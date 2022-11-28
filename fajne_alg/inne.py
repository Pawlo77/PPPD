import math


def multiply(A, B):
    assert len(A[0]) == len(B)
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for x in range(len(A[0])):
                C[i][j] += A[i][x] * B[x][j]

    return C


def warinacja(A):
    x_hat = sum(A) / len(A)

    sigma = 0.0
    for x in A:
        sigma += (x - x_hat) ** 2
    return sigma / len(A)


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


# k-elementowe kombinacje ze zbioru 0 ... n-1 bez zwracania
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
