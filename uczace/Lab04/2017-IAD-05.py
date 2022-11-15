import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import matplotlib.patches as patches


# def F(a, b):
    # iris = load_iris()
    # X, y = iris.data, iris.target
    # X, y = X[y != 0, :2], y[y != 0]
    
    # split = int(len(X) * 0.8)
    # order = np.random.permutation(len(X))

    # X = X[order]
    # y = y[order]

    # X_train, X_test = X[:split], X[split:]
    # y_train, y_test = y[:split], y[split:]

    # clf = SVC(gamma=a, C=b)
    # clf.fit(X_train, y_train)
    # return np.mean(clf.predict(X_test) == y_test)

def F(a, b): 
    iris = load_iris() # zbior iris
    X, y = iris.data, iris.target
    X, y = X[y != 0, :2], y[y != 0] # tylko klasy 1 i 2
    n_sample = len(X)
    np.random.seed(1234)
    order = np.random.permutation(n_sample)
    X = X[order]
    y = y[order].astype(np.float)
    X_train = X[:int(0.8 * n_sample)] # proba uczaca = losowe 80% 
    y_train = y[:int(0.8 * n_sample)]
    X_test = X[int(0.8 * n_sample):] # proba testowa = pozostale 20% 
    y_test = y[int(0.8 * n_sample):]
    clf = SVC(gamma=a, C=b) # support vector classifier
    clf.fit(X_train, y_train)
    return np.mean(clf.predict(X_test) == y_test)

def main():
    with open("input.txt") as f:
        (a1, an, n, b1, bm, m) = f.readlines()
    a1 = float(a1)
    an = float(an)
    n = int(n)
    b1 = float(b1)
    bm = float(bm)
    m = int(m)
    
    ar = (an - a1) / (n - 1)
    br = (bm - b1) / (m - 1)

    min_v, min_a, min_b = float("inf"), None, None
    max_v, max_a, max_b = 0, None, None

    l = max(len(str(max(an, bm))) + 2, 6)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlim([a1 - ar / 2, an + ar / 2])
    ax.set_ylim([b1 - br / 2, bm + br / 2])

    with open("output.txt", "w") as f:
        row = f"{'a, b':{l}.{l}s}|"
        b_c = b1
        for _ in range(m):
            row += f"{str(b_c):^{l}.{l}s}"
            b_c += br
        
        f.write(row + "\n")
        f.write(l * "-" + "|" + (len(row) - l - 1) * "-" + "\n")

        a_c = a1
        for _ in range(n):
            b_c = b1
            row = f"{str(a1):{l}.{l}s}|"

            for _ in range(m):
                s = F(a_c, b_c)
                if s > max_v:
                    max_v, max_a, max_b = s, a_c, b_c
                if s < min_v:
                    min_v, min_a, min_b = s, a_c, b_c

                ax.add_patch(patches.Rectangle(
                    (a_c - ar / 2, b_c - br / 2),
                    ar,
                    br,
                    facecolor=str(s)
                ))

                row += f"{str(s):^{l}.{l}s}"
                b_c += br
            
            f.write(row + "\n")
            a_c += ar

    fig.savefig("output.png", dpi=90)
    print(f"fmax = {max_v:2.2f}, dla a = {max_a}, b = {max_b}")
    print(f"fmin = {min_v:2.2f}, dla a = {min_a}, b = {min_b}")


if __name__ == '__main__':
    np.random.seed(1234)
    main()