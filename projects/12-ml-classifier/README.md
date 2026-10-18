# Machine Learning Classifier

Introductory ML classifier using scikit-learn and iris dataset.

## Features

- Train RandomForest on iris dataset
- Reproducible train/test split
- Accuracy, precision, recall, F1, confusion matrix
- Model serialization
- Prediction CLI

## Setup

```bash
cd projects/12-ml-classifier
python3 -m pip install scikit-learn --user
```

## Usage

```bash
cd projects/12-ml-classifier/src

# Train model
python cli.py train

# Make prediction (4 iris features)
python cli.py predict 5.1 3.5 1.4 0.2
```

## Testing

```bash
cd projects/12-ml-classifier
python tests/test_ml_classifier.py
```

## Dependencies

- Python 3.11+
- scikit-learn

## Limitations

- Uses bundled iris dataset (toy dataset)
- RandomForest with default params
- No hyperparameter tuning
- No cross-validation
- Educational only, not production-grade
