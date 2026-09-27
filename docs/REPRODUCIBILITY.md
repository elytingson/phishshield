# Reproducibility Guide

## Recommended environment

Python 3.11 or 3.12.

## Setup

```bash
python -m venv .venv
```

Activate the environment and install:

```bash
pip install -r requirements.txt
pip install -r requirements-optional.txt
```

## Data

Place:

```text
data/raw/PhiUSIIL_Phishing_URL_Dataset.csv
```

## Run order

1. Chapter 3 notebook
2. Chapter 4 notebook
3. Chapter 5 notebook

## Final model run

Use:

```python
FAST_MODE = False
```

before producing final report metrics.

## Random state

The notebooks use:

```python
RANDOM_STATE = 42
```

## Reproducibility artifacts

The modelling workflow saves:

- trained model pipelines
- champion models
- model comparison tables
- selected thresholds
- feature schemas
- environment configuration
- test-set metrics
- bias audit tables
- explainability figures

## Test policy

The held-out test set must not be used for:

- feature selection
- hyperparameter selection
- threshold selection
- champion selection
