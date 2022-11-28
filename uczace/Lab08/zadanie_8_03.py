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


def center(A):
    for i in range(len(A)):
        mean = sum(A[i]) / len(A[i])

        for j in range(len(A[i])):
            A[i][j] -= mean


def multiply(A, B):
    assert len(A[0]) == len(B)
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for x in range(len(A[0])):
                C[i][j] += A[i][x] * B[x][j]

    return C


def obrot(A, theta):
    B = [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
    return multiply(B, A)


def skalowanie(A, s):
    assert s > 0

    B = [[s, 0], [0, s]]
    return multiply(B, A)


def rozciaganie_X(A, m):
    assert m > 0

    B = [[1, m], [0, 1]]
    return multiply(B, A)


def rozciaganie_Y(A, m):
    assert m > 0

    B = [[1, 0], [m, 1]]
    return multiply(B, A)


def warinacja(A):
    x_hat = sum(A) / len(A)

    sigma = 0.0
    for x in A:
        sigma += (x - x_hat) ** 2
    return sigma / len(A)


def seek_highest(A, k):
    highest = -1
    highest_theta = None

    for i in range(k):
        theta = i * math.pi / k
        C = obrot(A, theta)[0]
        cur = warinacja(C)

        if cur > highest:
            highest_theta = theta
            highest = cur

    return highest_theta


def plot_przebieg(A):
    k = 100
    wektor_theta = [i * math.pi / k for i in range(k)]
    wektor_v_x = [0 for _ in range(k)]
    wektor_v_y = [0 for _ in range(k)]

    for i in range(k):
        C = obrot(A, wektor_theta[i])

        wektor_v_x[i] = warinacja(C[0])
        wektor_v_y[i] = warinacja(C[1])

    plt.plot(wektor_theta, wektor_v_x, "r-")
    plt.plot(wektor_theta, wektor_v_y, "b--")
    plt.savefig("output_theta.png")


def plot(A, C, k):
    plt.figure(figsize=[8, 4], dpi=72)
    plt.subplot(1, 2, 1)  # lewy wykres - zbiór oryginalny
    plt.scatter(A[0], A[1])
    plt.subplot(1, 2, 2)  # prawy wykres - zbiór przekształcony
    plt.scatter(C[0], C[1])
    plt.savefig(f"output_przeksztalcenie{k}.png")


def main():
    cols = ["sepal length", "sepal width", "petal length", "petal width"]

    A = load()
    print("shape:", len(A), len(A[0]))

    A = transpose(A)
    print("shape:", len(A), len(A[0]))

    B = [A[0], A[1]]
    print("shape:", len(B), len(B[0]))

    center(B)

    C = obrot(B, math.pi / 4)
    plot(B, C, 1)

    C = skalowanie(B, 5.1)
    plot(B, C, 2)

    C = rozciaganie_X(B, 1.5)
    plot(B, C, 3)

    C = rozciaganie_Y(B, 1.5)
    plot(B, C, 4)

    print(f"Najwieksza znaleziona warinacja dla theta={seek_highest(B, 100)}pi")

    plot_przebieg(B)


if __name__ == "__main__":
    main()
