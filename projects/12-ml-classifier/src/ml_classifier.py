"""Machine Learning Classifier - sklearn wrapper."""
from pathlib import Path
import pickle
from typing import Dict, Tuple


try:
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False


class MLClassifier:
    """Simple ML classifier wrapper."""
    
    def __init__(self):
        if not SKLEARN_AVAILABLE:
            raise ImportError("Install: python3 -m pip install scikit-learn --user")
        self.model = None
        self.feature_names = []
        self.target_names = []
    
    def load_iris_dataset(self) -> Tuple:
        """Load iris dataset."""
        data = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(
            data.data, data.target, test_size=0.2, random_state=42
        )
        self.feature_names = data.feature_names
        self.target_names = data.target_names.tolist()
        return X_train, X_test, y_train, y_test
    
    def train(self, X_train, y_train):
        """Train RandomForest classifier."""
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
    
    def evaluate(self, X_test, y_test) -> Dict:
        """Evaluate model."""
        if not self.model:
            raise ValueError("Model not trained")
        
        y_pred = self.model.predict(X_test)
        
        return {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted', zero_division=0),
            'recall': recall_score(y_test, y_pred, average='weighted', zero_division=0),
            'f1': f1_score(y_test, y_pred, average='weighted', zero_division=0),
            'confusion_matrix': confusion_matrix(y_test, y_pred).tolist()
        }
    
    def predict(self, X):
        """Make predictions."""
        if not self.model:
            raise ValueError("Model not trained")
        return self.model.predict(X)
    
    def save_model(self, path: Path):
        """Save model to file."""
        # ponytail: pickle is safe here - user loads only their own trained models
        with open(path, 'wb') as f:
            pickle.dump({
                'model': self.model,
                'feature_names': self.feature_names,
                'target_names': self.target_names
            }, f)
    
    def load_model(self, path: Path):
        """Load model from file."""
        with open(path, 'rb') as f:
            data = pickle.load(f)
            self.model = data['model']
            self.feature_names = data['feature_names']
            self.target_names = data['target_names']
