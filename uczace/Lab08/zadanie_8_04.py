import csv
import math
import random
import numpy as np
import itertools
import matplotlib.pyplot as plt


def load():
    iris = []
    f = open("iris.csv", "r")  # r=do odczytu
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = float(row[i])  # konwersja z str na float
        list.append(iris, row)  # == A.append(row)
    f.close()
    return iris


def transpose(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]


def zaburz(X):
    for i in range(len(X)):
        for j in range(len(X[0])):
            X[i][j] += random.uniform(-0.05, 0.05)


def get_centroid(A):
    C = []

    for i in range(len(A)):
        c1 = sum(A[i][:50]) / 50
        c2 = sum(A[i][50:100]) / 50
        c3 = sum(A[i][100:]) / 50

        C.append([c1, c2, c3])
    return C


def plot(X, cols):
    plt.figure(figsize=[16, 16], dpi=72)
    plt.tight_layout
    n = len(X)

    colors = [None for _ in range(len(X[0]))]
    for i in range(len(X[0])):
        if i < 50:
            colors[i] = "red"
        elif i < 100:
            colors[i] = "green"
        else:
            colors[i] = "blue"

    centroids = get_centroid(X)

    c = 1
    for i in range(n):
        for j in range(n):
            plt.subplot(n, n, c)

            plt.scatter(X[i], X[j], c=colors, alpha=0.3)
            plt.xlabel(cols[i])
            plt.ylabel(cols[j])

            plt.plot(
                centroids[i],
                centroids[j],
                markersize=25,
                color="#00000055",
                marker="o",
                linestyle="",
            )

            c += 1

    plt.savefig("output2.png")


def get_distance(v1, v2):
    sigma = 0
    for x, y in zip(v1, v2):
        sigma += (x - y) ** 2
    return math.sqrt(sigma)


def power(x):
    p = 1
    for i in range(2, x + 1):
        p *= i
    return p


def get_all_comb(n, k):
    res = []
    temp = []

    def helper(left, k):
        if k == 0:
            res.append(temp.copy())
        else:
            for i in range(left, n + 1):
                temp.append(i)
                helper(i + 1, k - 1)
                temp.pop()

    helper(0, k)
    return res


def check_proportion(X):
    centroids = np.array(get_centroid(X))
    X = np.array(X)

    for j in range(1, 5):
        for comb in get_all_comb(3, j):
            not_from_closest_class = 0

            for i in range(len(X[0])):
                pkt = X[comb, i]

                v0 = get_distance(pkt, centroids[comb, 0])
                v1 = get_distance(pkt, centroids[comb, 1])
                v2 = get_distance(pkt, centroids[comb, 2])

                v = [v0, v1, v2]
                id = v.index(min(v))

                if (
                    (100 <= id < 150 and id != 2)
                    or (50 <= id < 100 and id != 1)
                    or (i < 50 and id != 0)
                ):
                    not_from_closest_class += 1

            print(f"{comb}: {not_from_closest_class / len(X[0])}")


def std(X, x_m):
    sigma = 0.0
    for x in X:
        sigma += (x - x_m) ** 2
    return math.sqrt(sigma / len(X))


def standarize(X):
    for i in range(len(X)):
        x_m = sum(X[i]) / len(X[i])
        x_s = std(X[i], x_m)

        for j in range(len(X[i])):
            X[i][j] = (X[i][j] - x_m) / x_s


def main():
    cols = ["sepal length", "sepal width", "petal length", "petal width"]

    A = load()
    print("shape:", len(A), len(A[0]))

    A = transpose(A)
    print("shape:", len(A), len(A[0]))

    zaburz(A)
    plot(A, cols)

    print()
    print("Unstandarized")
    check_proportion(A)

    standarize(A)

    print()
    print("Standarized")
    check_proportion(A)


if __name__ == "__main__":
    main()
