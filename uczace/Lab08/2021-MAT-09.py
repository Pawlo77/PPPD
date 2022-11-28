import random
import math
import matplotlib.pyplot as plt

# wyniki nie takie jak w tresci ???


def macierz_startowa(n):
    return [[1 if i != j else 0 for i in range(n)] for j in range(n)]


def deg(A, n, i):
    d = 0
    for j in range(n):
        d += A[i][j]
    return d


def licznosc_stopni(A):
    n = len(A)
    D = [deg(A, n, i) for i in range(n)]
    dim = max(D)

    K = [0 for _ in range(dim + 1)]
    for d in D:
        K[d] += 1
    return K


def nowe_grono(A, N, m):
    n = len(A)
    B = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(n):
        for j in range(n):
            B[i][j] = A[i][j]

    for i in range(n, N):
        znaj = list(range(i))
        nowi_znaj = random.sample(znaj, m)

        for nowy_znaj in nowi_znaj:
            B[i][nowy_znaj] = 1
            B[nowy_znaj][i] = 1

    return B


def p(k, m):
    if k < m:
        return 0
    return math.e ** (1 - k / m) / m


def srednie_bledy(T):
    N = 100
    m = 3
    n = 5

    A = macierz_startowa(n)
    V = [0 for _ in range(N)]

    for i in range(T):
        B = nowe_grono(A, N, m)
        k = licznosc_stopni(B)

        for j in range(N):
            if j < len(k):
                V[j] += k[j] - N * p(j, m)
            else:
                V[j] += 0 - N * p(j, m)

    for i in range(N):
        V[i] /= T
    return V


def main():
    random.seed(126)

    A = macierz_startowa(4)
    l = licznosc_stopni(A)

    for row in A:
        print(row)
    print(l)

    print()
    B = nowe_grono(A, 6, 2)
    for row in B:
        print(row)

    print()
    sb = srednie_bledy(1000)
    print(sb[:5])

    plt.scatter(list(range(len(sb))), sb)
    plt.show()


if __name__ == "__main__":
    main()
