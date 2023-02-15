from linear_algebra import distance, Vector
from typing import List
from Flower import Flower
from collections import Counter


def classify(k: int, training_points: List[Flower], new_point: Vector) -> str:
    """Simple classifier"""
    sorted_set = sorted(training_points, key=lambda tp: distance(tp.point, new_point))
    sorted_set = sorted_set[:k]
    labels = [flower.label for flower in sorted_set]
    return find_winner(labels)


def find_winner(labels: List[str]):
    """Determining which label is mode."""
    cnt = Counter(labels)
    mode, _ = cnt.most_common(1)[0]
    return mode
