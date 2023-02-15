import pandas as pd
from data_processing import parse_data, group_flowers, split_data
from data_visualization import plot_features
from classifier import classify
from constants import K_NEAREST_NEIGHBORS, SPLIT_RATIO


if __name__ == '__main__':

    # Reading data
    raw_data = pd.read_csv('iris.data', header=None)

    # Data processing
    flowers = parse_data(raw_data)
    flowers_by_species = group_flowers(flowers)

    # Data visualization
    plot_features(flowers_by_species)

    # Splitting data
    train_set, test_set = split_data(flowers, SPLIT_RATIO)

    # Classification
    wrong_predicts = 0

    for flower in test_set:
        predicted = classify(K_NEAREST_NEIGHBORS, train_set, flower.point)
        actual = flower.label
        if actual != predicted:
            wrong_predicts += 1
            print("WRONG! ", end='')
        print("Predicted: " + predicted + " | Actual: " + actual)

    # Accuracy
    print((len(test_set) - wrong_predicts) / len(test_set))
