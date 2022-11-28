import math
import matplotlib.pyplot as plt


def load_X(name):
    with open(name) as f:
        X = [line.strip().split(",") for line in f.readlines()]

    for i in range(len(X)):
        X[i] = [float(X[i][0]), float(X[i][1])]

        assert len(X[i]) == 2, "Zły wymiar macierzy"
    return X


def load_y(name):
    with open(name) as f:
        y = [int(line.strip()) for line in f.readlines()]

    for val in y:
        assert val in [0, 1], "Bledna wartosc klasy"
    return y


def distance(u, v):
    dist = 0
    for i in range(len(u)):
        dist += (u[i] - v[i]) ** 2
    return math.sqrt(dist)


def nearest_neighbor_class(A, c, z):
    best_i = None
    best_dist = None

    for i in range(len(A)):
        dist = distance(A[i], z)

        if best_dist is None or best_dist > dist:
            best_dist = dist
            best_i = i

    return c[best_i]


def knn(A, c, Z):
    l = [None] * len(Z)

    for i in range(len(Z)):
        l[i] = nearest_neighbor_class(A, c, Z[i])

    return l


def generate_x_y(A, n):
    a_max = b_max = -float("inf")
    a_min = b_min = float("inf")

    for row in A:
        if row[0] > a_max:
            a_max = row[0]
        if row[0] < a_min:
            a_min = row[0]
        if row[1] > b_max:
            b_max = row[1]
        if row[1] < b_min:
            b_min = row[1]

    r = (a_max - a_min) / (n - 1)
    t = (b_max - b_min) / (n - 1)

    x = [a_min + r * i for i in range(n)]
    y = [b_min + t * i for i in range(n)]
    return x, y


def plot(A, c, n):
    x, y = generate_x_y(A, n)

    for i in range(n):
        for j in range(n):
            y_pred = knn(A, c, [[x[i], y[j]]])[0]

            color = "r" if y_pred == 0 else "g"
            plt.scatter(x[i], y[j], color=color, alpha=0.2, marker=".")

    for i in range(len(A)):
        color = "r" if c[i] == 0 else "g"
        plt.scatter(A[i][0], A[i][1], color=color)

    plt.savefig("output.png", dpi=90)


def test_quality(y_true, y_pred):
    TN = FP = FN = TP = 0

    for i in range(len(y_true)):
        if y_true[i] == y_pred[i] == 0:
            TN += 1
        elif y_true[i] == y_pred[i] == 1:
            TP += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            FN += 1
        else:
            FP += 1

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1_score = 2 * TP / (2 * TP + FP + FN)

    print(f"  |{'0':^10}|{'1':^10}")
    print("-" * 25)
    print(f"0 |{TN:^10}|{FP:^10}")
    print(f"1 |{FN:^10}|{TP:^10}")

    print()
    for name, score in (
        ("dokladnosc", accuracy),
        ("precyzja", precision),
        ("czulosc", recall),
        ("miara f1", f1_score),
    ):
        print(f"{name:s<10} = {score:1.3f}")


def main():
    X_train = load_X("train_wine.csv")
    y_train = load_y("train_class.txt")
    assert len(X_train) == len(y_train), "podane X i y maja rozne ilosci rekordow"

    plot(X_train, y_train, 100)

    X_test = load_X("test_wine.csv")
    y_test = load_y("test_class.txt")
    assert len(X_test) == len(y_test), "podane X i y maja rozne ilosci rekordow"

    y_pred = knn(X_train, y_train, X_test)
    test_quality(y_test, y_pred)


if __name__ == "__main__":
    main()
