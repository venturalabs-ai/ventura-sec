from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    failed_logins: int
    unique_sources: int
    sensitive_actions: int
    off_hours: bool = False


def anomaly_score(event: Event) -> float:
    """Deterministic defensive risk score for synthetic/authorized event triage."""
    if min(event.failed_logins, event.unique_sources, event.sensitive_actions) < 0:
        raise ValueError("event counters must be non-negative")
    score = 0.0
    score += min(event.failed_logins / 10, 1.0) * 0.35
    score += min(max(event.unique_sources - 1, 0) / 5, 1.0) * 0.25
    score += min(event.sensitive_actions / 5, 1.0) * 0.30
    score += 0.10 if event.off_hours else 0.0
    return round(min(score, 1.0), 4)


def classify(event: Event, threshold: float = 0.5) -> bool:
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    return anomaly_score(event) >= threshold


def precision_recall(labels: list[bool], predictions: list[bool]) -> tuple[float, float]:
    if len(labels) != len(predictions) or not labels:
        raise ValueError("labels and predictions must be non-empty and aligned")
    tp = sum(label and prediction for label, prediction in zip(labels, predictions))
    fp = sum((not label) and prediction for label, prediction in zip(labels, predictions))
    fn = sum(label and (not prediction) for label, prediction in zip(labels, predictions))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    return precision, recall
