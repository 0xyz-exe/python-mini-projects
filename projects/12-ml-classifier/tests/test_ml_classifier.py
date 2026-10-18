"""Tests for ML classifier."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

try:
    from ml_classifier import MLClassifier
    import sklearn
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False


def test_train_and_evaluate():
    if not SKLEARN_AVAILABLE:
        return
    
    classifier = MLClassifier()
    X_train, X_test, y_train, y_test = classifier.load_iris_dataset()
    
    classifier.train(X_train, y_train)
    metrics = classifier.evaluate(X_test, y_test)
    
    assert 'accuracy' in metrics
    assert metrics['accuracy'] > 0.8


def test_save_load_model():
    if not SKLEARN_AVAILABLE:
        return
    
    with TemporaryDirectory() as tmpdir:
        model_path = Path(tmpdir) / "model.pkl"
        
        classifier = MLClassifier()
        X_train, X_test, y_train, y_test = classifier.load_iris_dataset()
        classifier.train(X_train, y_train)
        
        classifier.save_model(model_path)
        
        classifier2 = MLClassifier()
        classifier2.load_model(model_path)
        
        predictions = classifier2.predict(X_test)
        assert len(predictions) == len(y_test)


if __name__ == "__main__":
    if not SKLEARN_AVAILABLE:
        print("⚠ scikit-learn not available - tests skipped")
        exit(0)
    
    test_train_and_evaluate()
    test_save_load_model()
    print("✓ All tests passed")
