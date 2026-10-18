#!/usr/bin/env python3
"""ML Classifier CLI."""
import argparse
from pathlib import Path
from ml_classifier import MLClassifier


def main():
    parser = argparse.ArgumentParser(description="ML classifier")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    subparsers.add_parser("train", help="Train model on iris dataset")
    
    predict = subparsers.add_parser("predict", help="Predict from model")
    predict.add_argument("values", nargs=4, type=float, help="4 feature values")
    
    args = parser.parse_args()
    model_path = Path("iris_model.pkl")
    
    try:
        classifier = MLClassifier()
        
        if args.command == "train":
            print("Loading iris dataset...")
            X_train, X_test, y_train, y_test = classifier.load_iris_dataset()
            
            print("Training RandomForest...")
            classifier.train(X_train, y_train)
            
            print("Evaluating...")
            metrics = classifier.evaluate(X_test, y_test)
            
            print(f"\nAccuracy:  {metrics['accuracy']:.3f}")
            print(f"Precision: {metrics['precision']:.3f}")
            print(f"Recall:    {metrics['recall']:.3f}")
            print(f"F1:        {metrics['f1']:.3f}")
            
            print(f"\nConfusion Matrix:")
            for row in metrics['confusion_matrix']:
                print(row)
            
            classifier.save_model(model_path)
            print(f"\n✓ Model saved to {model_path}")
        
        elif args.command == "predict":
            if not model_path.exists():
                print(f"Error: Model not found. Run 'train' first.")
                return 1
            
            classifier.load_model(model_path)
            prediction = classifier.predict([args.values])
            class_name = classifier.target_names[prediction[0]]
            
            print(f"Prediction: {class_name} (class {prediction[0]})")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
