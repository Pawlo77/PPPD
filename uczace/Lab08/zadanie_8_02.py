import csv
import math
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


def plot(X, cols):
    plt.figure(figsize=[16, 16], dpi=72)
    plt.tight_layout
    n = len(X)

    c = 1
    for i in range(n):
        for j in range(n):
            plt.subplot(n, n, c)

            plt.scatter(X[i], X[j], alpha=0.6)
            plt.xlabel(cols[i])
            plt.ylabel(cols[j])

            alpha, beta = lr(X[i], X[j])
            f = lambda x: alpha * x + beta

            x_0, x_1 = min(X[i]), max(X[i])
            plt.plot([x_0, x_1], [f(x_0), f(x_1)])

            c += 1

    plt.savefig("output.png")


def lr(x, y):
    x_hat = sum(x) / len(x)
    y_hat = sum(y) / len(y)

    up = down = 0
    for x_i, y_i in zip(x, y):
        up += (x_i - x_hat) * (y_i - y_hat)
        down += (x_i - x_hat) ** 2
    beta = up / down

    return beta, y_hat - beta * x_hat


def std(x):
    res = 0.0

    x_hat = sum(x) / len(x)
    for x_i in x:
        res += (x_i - x_hat) ** 2

    return math.sqrt(res / (len(x) - 1))


def corr(x, y):
    x_hat = sum(x) / len(x)
    y_hat = sum(y) / len(y)
    s_x = std(x)
    s_y = std(y)

    sigma = 0.0
    for x_i, y_i in zip(x, y):
        sigma += ((x_i - x_hat) / s_x) * ((y_i - y_hat) / s_y)

    return 1 / (len(x) - 1) * sigma


def main():
    cols = ["sepal length", "sepal width", "petal length", "petal width"]

    X = load()
    print("shape:", len(X), len(X[0]))

    X = transpose(X)
    print("shape:", len(X), len(X[0]))

    plot(X, cols)

    corr_matrix = [[corr(X[i], X[j]) for i in range(len(X))] for j in range(len(X))]
    for row in corr_matrix:
        print(row)


if __name__ == "__main__":
    main()
