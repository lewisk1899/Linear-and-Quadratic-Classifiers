# Lewis Koplon
# ECE 523 Engineering Applications of Machine Learning and Data Analytics
# Professor Ditzler
# Linear and Quadratic Classifiers

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


def normal_samples():
    samples = 100
    # distribution 1
    mean_1 = np.array([0, 0])  # mean vector which is the 0 vector for simplicity
    mean_2 = np.array([-2.6, -2])
    mean_3 = np.array([2, 3])
    covariance_matrix = np.identity(2)  # covariance matrix is the identity matrix
    # we will be sampling from a standard normal distribution, this will produce 30 sample with d features [x1, x2, x3... xd]
    dataset = []
    # training set
    for i in range(samples):
        dataset.append(np.random.multivariate_normal(mean_1, covariance_matrix))
    for i in range(samples):
        dataset.append(np.random.multivariate_normal(mean_2, covariance_matrix))
    for i in range(samples):
        dataset.append(np.random.multivariate_normal(mean_3, covariance_matrix))
    return dataset, mean_1, mean_2, mean_3, covariance_matrix


def test_samples():
    samples = 30
    # distribution 1
    mean_1 = np.array([0, 0])  # mean vector which is the 0 vector for simplicity
    mean_2 = np.array([-2.6, -2])
    mean_3 = np.array([2, 3])
    covariance_matrix = np.identity(2)  # covariance matrix is the identity matrix
    # we will be sampling from a standard normal distribution, this will produce 30 sample with d features [x1, x2, x3... xd]
    dataset = []
    # training set
    for i in range(samples):
        dataset.append(np.random.multivariate_normal(mean_1, covariance_matrix))
    for i in range(samples):
        dataset.append(np.random.multivariate_normal(mean_2, covariance_matrix))
    for i in range(samples):
        dataset.append(np.random.multivariate_normal(mean_3, covariance_matrix))
    return dataset, mean_1, mean_2, mean_3, covariance_matrix


def classify():
    dimensions = 2
    prob_of_class_1 = prob_of_class_2 = prob_of_class_3 = 33.33
    dataset, mean_1, mean_2, mean_3, covariance_matrix = normal_samples()
    mean_1 = mean_1[np.newaxis]
    mean_2 = mean_2[np.newaxis]
    mean_3 = mean_3[np.newaxis]
    classified_data = []
    for sample in dataset:
        sample = sample[np.newaxis]
        g_x_1 = -.5 * np.matmul(np.matmul((sample - mean_1), np.linalg.inv(covariance_matrix)), (sample - mean_1).T) \
                - .5 * dimensions * np.log(2 * np.pi) - .5 * np.log(
            np.linalg.det(covariance_matrix)) + np.log(prob_of_class_1)
        g_x_2 = -.5 * np.matmul(np.matmul((sample - mean_2), np.linalg.inv(covariance_matrix)), (sample - mean_2).T) \
                - .5 * dimensions * np.log(2 * np.pi) - .5 * np.log(np.linalg.det(covariance_matrix)) + np.log(
            prob_of_class_2)
        g_x_3 = -.5 * np.matmul(np.matmul((sample - mean_3), np.linalg.inv(covariance_matrix)), (sample - mean_3).T) \
                - .5 * dimensions * np.log(2 * np.pi) - .5 * np.log(np.linalg.det(covariance_matrix)) + np.log(
            prob_of_class_3)
        classified_data.append((sample, g_x_1, g_x_2, g_x_3))
    # what class does this belong to?
    class_1 = []
    class_2 = []
    class_3 = []
    # assigning to classes
    for sample in classified_data:
        print("Class 1:")
        print(sample[0][0])
        print(sample[1][0])
        print("##########################################")
        print("Class 2:")
        print(sample[0][0])
        print(sample[2][0])
        print("##########################################")
        print("Class 3:")
        print(sample[0][0])
        print(sample[3][0])
        print("##########################################")

        if sample[1][0] >= sample[2][0] and sample[1][0] >= sample[3][0]:
            class_1.append(sample[0])
        elif sample[2][0] >= sample[1][0] and sample[2][0] >= sample[3][0]:
            class_2.append(sample[0])
        elif sample[3][0] >= sample[1][0] and sample[3][0] >= sample[2][0]:
            class_3.append(sample[0])
    graph(class_1, class_2, class_3)


def graph(class_1, class_2, class_3):
    fig, ax = plt.subplots()
    print(" Data Points this algorithm thinks is generated by class_1", len(class_1))
    print(" Data Points this algorithm thinks is generated by class_2", len(class_2))
    print(" Data Points this algorithm thinks is generated by class_3", len(class_3))
    for point in class_1:
        print("x1 = ", point[0][0], "x2 =", point[0][1])
        scatter = ax.scatter(point[0][0], point[0][1], c='#1f77b4')  # Blue
    for point in class_2:
        print("x1 = ", point[0][0], "x2 =", point[0][1])
        ax.scatter(point[0][0], point[0][1], c='#ff7f0e')
    for point in class_3:
        print("x1 = ", point[0][0], "x2 =", point[0][1])
        ax.scatter(point[0][0], point[0][1], c='#2ca02c')  # Green
    plt.xlabel("X1")
    plt.ylabel("X2")
    ax.set(xlim=(-6, 6), xticks=np.arange(-6, 6), ylim=(-6, 6), yticks=np.arange(-6, 6))
    legend_elements = [Line2D([0], [0], linewidth=0, marker='.', mfc='#1f77b4', mec='#1f77b4', label='Class 1',
                              markersize=10),
                       Line2D([0], [0], linewidth=0, marker='.', mfc='#ff7f0e', mec='#ff7f0e', label='Class 2',
                              markersize=10),
                       Line2D([0], [0], linewidth=0, marker='.', mfc='#2ca02c', mec='#2ca02c', label='Class 3',
                              markersize=10)]
    ax.legend(handles=legend_elements, loc='upper right')
    ax.grid(True)
    plt.show()


def mahalanobis_distance(point, mu, cov):
    return np.matmul(np.matmul((point - mu), np.linalg.inv(cov)), (point - mu).T)[0]


classify()
