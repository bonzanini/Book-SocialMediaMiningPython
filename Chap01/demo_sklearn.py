# Chap01/demo_sklearn.py
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Load the data
    iris = datasets.load_iris()
    X = iris.data
    petal_length = X[:, 2]
    petal_width = X[:, 3]
    true_labels = iris.target
    # Apply KMeans clustering
    estimator = KMeans(n_clusters=3)
    estimator.fit(X)
    predicted_labels = estimator.labels_
    # Color scheme definition: red, yellow and blue
    color_scheme = ['r', 'y', 'b']
    # Markers definition: circle, "x" and "plus"
    marker_list = ['x', 'o', '+']
    # Assign colors/markers to the predicted labels
    colors_predicted_labels = [color_scheme[lab] for lab in predicted_labels]
    markers_predicted = [marker_list[lab] for lab in predicted_labels]
    # Assign colors/markers to the true labels
    colors_true_labels = [color_scheme[lab] for lab in true_labels]
    markers_true = [marker_list[lab] for lab in true_labels]
    # Plot and save the two scatter plots
    for x, y, c, m in zip(petal_width,
                          petal_length,
                          colors_predicted_labels,
                          markers_predicted):
        plt.scatter(x, y, c=c, marker=m)
    plt.savefig('iris_clusters.png')
    for x, y, c, m in zip(petal_width,
                          petal_length,
                          colors_true_labels,
                          markers_true):
        plt.scatter(x, y, c=c, marker=m)
    plt.savefig('iris_true_labels.png')

    print(iris.target_names)
