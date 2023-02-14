from typing import List
import math

Vector = List[float]


def distance(v: Vector, u: Vector) -> float:
    """Calculating Euclidean distance between two points."""
    sigma = 0.0
    for i in range(len(v)):
        sigma += (v[i] - u[i]) ** 2
    return math.sqrt(sigma)
