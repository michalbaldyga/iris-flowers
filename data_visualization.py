import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')


def plot_features(flowers):
    """Plotting the features to see how they differ by species."""
    features = ['sepal length', 'sepal width', 'petal length', 'petal width']
    features_to_explore = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    marks = ['+', 'p', '*']
    figure, axis = plt.subplots(2, 3)
    figure.set_size_inches(16, 9)
    axis_x = 0
    axis_y = 0

    for pair in features_to_explore:
        for mark, (label, points) in zip(marks, flowers.items()):
            xs = [points_i[pair[0]] for points_i in flowers[label]]
            ys = [points_i[pair[1]] for points_i in flowers[label]]
            axis[axis_x, axis_y].scatter(xs, ys, marker=mark, label=label)
            axis[axis_x, axis_y].set_title(features[pair[0]] + " vs " + features[pair[1]])
        axis_y += 1
        if axis_y == 3:
            axis_x += 1
            axis_y = 0

    plt.legend()
    plt.show()