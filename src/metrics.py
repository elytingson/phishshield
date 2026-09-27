"""Common evaluation metrics for PhishShield."""

from __future__ import annotations

import numpy as np
from sklearn.metrics import confusion_matrix


def false_positive_rate(y_true, y_pred) -> float:
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    return fp / (fp + tn) if (fp + tn) else float("nan")


def threshold_predictions(scores, threshold: float):
    return (np.asarray(scores) >= threshold).astype(int)
