import random


def wypisz_macierz(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if type(matrix[row][column]) is float:
                print(f"{matrix[row][column]:6.2}", end=" ")
            else:
                print(f"{matrix[row][column]:6}", end=" ")
        print()
    print()


def losuj_macierz(wiersze, kolumny, a, b):
    return [[random.randint(a, b) for j in range(kolumny)] for i in range(wiersze)]


def losuj_wektor(n, a, b):
    return [random.randint(a, b) for j in range(n)]


def mnoz_macierz_wektor(A, b):
    res = [None for _ in range(len(A))]

    for i in range(len(A)):
        s = 0
        for j in range(len(b)):
            s += b[j] * A[i][j]
        res[i] = s

    return res


def macierz_vandermonde(alfa, n):
    res = [[1 for _ in range(n)] for _ in range(len(alfa))]

    for i in range(len(alfa)):
        a = 1

        for j in range(1, n):
            a *= alfa[i]
            res[i][j] = a

    return res


def czy_macierz_permutacji(macierz):
    s_rows = [0 for _ in range(len(macierz))]
    s_cols = [0 for _ in range(len(macierz[0]))]

    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            s_rows[i] += macierz[i][j]
            s_cols[j] += macierz[i][j]

    return max(s_rows) <= 1 and max(s_cols) <= 1


def main():
    random.seed(123)

    M = losuj_macierz(3, 4, 0, 4)
    v = losuj_wektor(4, 0, 4)

    print("Macierz:")
    wypisz_macierz(M)
    print("Wektor:")
    print(v)
    print("Iloczyn:")
    print(mnoz_macierz_wektor(M, v))

    alfa = [1, 2, 3, 5, 7]
    n = 4
    print("Macierz Vandermonde'a:")
    wypisz_macierz(macierz_vandermonde(alfa, n))

    macierz_permutacji = [[None for _ in range(3)] for _ in range(3)]
    macierz_permutacji[0][0] = macierz_permutacji[1][0] = 0
    macierz_permutacji[2][0] = 1
    macierz_permutacji[1][1] = macierz_permutacji[2][1] = 0
    macierz_permutacji[0][1] = 1
    macierz_permutacji[0][2] = macierz_permutacji[2][2] = 0
    macierz_permutacji[1][2] = 1

    print("Macierz permutacji:")
    wypisz_macierz(macierz_permutacji)
    print("Czy macierz permutacji: ", czy_macierz_permutacji(macierz_permutacji))
    macierz_permutacji[0][0] = 1
    wypisz_macierz(macierz_permutacji)
    print("Czy macierz permutacji: ", czy_macierz_permutacji(macierz_permutacji))


if __name__ == "__main__":
    main()
