import random


def wypisz_macierz(matrix):
    print(" ", end=" ")

    for column in range(len(matrix[0])):
        if column < 10:
            print(column, end=" ")
        else:
            print(chr(ord("A") + column - 10), end=" ")
    print()

    for row in range(len(matrix)):
        if row < 10:
            print(row, end=" ")
        else:
            print(chr(ord("A") + row - 10), end=" ")
        for column in range(len(matrix[row])):
            print(f"{matrix[row][column]}", end=" ")
        print()
    print()


def losuj_miny(plansza, liczba_min):
    while liczba_min:
        x = random.randint(0, len(plansza) - 1)
        y = random.randint(0, len(plansza[0]) - 1)

        if plansza[x][y] != 9:
            plansza[x][y] = 9
            liczba_min -= 1


def wypisz_macierz_cenzura(plansza, cenzura):
    print(" ", end=" ")

    for column in range(len(plansza[0])):
        if column < 10:
            print(column, end=" ")
        else:
            print(chr(ord("A") + column - 10), end=" ")
    print()

    for i in range(len(plansza)):
        if i < 10:
            print(i, end=" ")
        else:
            print(chr(ord("A") + i - 10), end=" ")

        for j in range(len(plansza[0])):
            if cenzura[i][j]:
                print(plansza[i][j], end=" ")
            else:
                print("*", end=" ")
        print()


def odkryj_pole(plansza, cenzura, wiersz, kolumna):
    if 0 <= wiersz < len(plansza) and 0 <= kolumna < len(plansza[0]):
        if plansza[wiersz][kolumna] != 9:
            cenzura[wiersz][kolumna] = True
            return True
    return False


def numery_przy_minach(plansza):
    for i in range(len(plansza)):
        for j in range(len(plansza[0])):
            if plansza[i][j] == 9:
                continue

            c = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if not x == y == 0:
                        if (
                            0 <= i + x < len(plansza)
                            and 0 <= j + y < len(plansza[0])
                            and plansza[i + x][j + y] == 9
                        ):
                            c += 1

            plansza[i][j] = c


def main():
    plansza = [[0 for _ in range(15)] for _ in range(10)]
    cenzura = [[False for _ in range(15)] for _ in range(10)]

    losuj_miny(plansza, 15)
    numery_przy_minach(plansza)
    wypisz_macierz(plansza)
    wypisz_macierz_cenzura(plansza, cenzura)

    for _ in range(5):
        wiersz = int(input("wiersz: "))
        kolumna = int(input("kolumna: "))

        if not odkryj_pole(plansza, cenzura, wiersz, kolumna):
            print("PRZEGRALES!")
            break
        wypisz_macierz_cenzura(plansza, cenzura)


if __name__ == "__main__":
    random.seed(42)
    main()
