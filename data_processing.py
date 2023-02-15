from constants import FEATURES_NO
from collections import defaultdict


class Flower:
    """Exemplary flower object: ([5.1, 3.5, 1.4, 0.2], 'Iris-setosa')"""
    def __init__(self, point, label):
        self.point = point
        self.label = label


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