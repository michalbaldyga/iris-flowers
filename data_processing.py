from constants import FEATURES_NO
from collections import defaultdict
from Flower import Flower
from random import shuffle
from typing import List, Tuple


def parse_data(data):
    """Parsing raw data into a useful form."""
    elements = []
    for i in range(len(data)):
        point = [data.iloc[i][j] for j in range(FEATURES_NO - 1)]
        label = data.iloc[i][FEATURES_NO - 1]
        elements.append(Flower(point, label))
    return elements


def group_flowers(flowers):
    """Grouping flowers by species."""
    flowers_by_species = defaultdict(list)
    for flower in flowers:
        flowers_by_species[flower.label].append(flower.point)
    return flowers_by_species


def split_data(dataset: List[Flower], split: float) -> Tuple[List[Flower], List[Flower]]:
    """Splitting dataset into training set and testing set."""
    data = dataset.copy()
    shuffle(data)
    split_idx = int(split * len(data))
    return data[:split_idx], data[split_idx:]
