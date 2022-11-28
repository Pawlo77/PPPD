import csv


def wczytaj_dane(sciezka):
    M = []
    f = open(sciezka)
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = int(row[i])  # konwersja z str na int
        list.append(M, row)  # == A.append(row)
    f.close()
    return M


def wypisz(dane):
    l = len(str(len(dane) - 1))

    print(l * " " + "  ", end="")
    print(" ".join([str(i) for i in range(len(dane[0]))]))

    for i in range(len(dane)):
        print(f"{i:<{l}d}: ", end="")

        for j in range(len(dane[0])):
            if j < 10:
                l_c = 1
            else:
                l_c = 2
            print(f"{dane[i][j]:<{l_c}d} ", end="")

        print()


def bezpieczne(row, lista):
    for alergen in lista:
        if row[alergen]:
            return False
    return True


def szukaj_bezpiecznych_dan(dane, lista):
    return [i for i in range(len(dane)) if bezpieczne(dane[i], lista)]


def dodaj_nowe_danie(dane, lista):
    nowe = [None for _ in range(len(dane) + 1)]

    for i in range(len(dane)):
        nowe[i] = dane[i].copy()

    nowe_danie = [0 for _ in range(len(dane[0]))]
    for alergen in lista:
        nowe_danie[alergen] = 1
    nowe[len(dane)] = nowe_danie

    return nowe


def dobry(row, k):
    return sum(row) < k


def usun_najgorsze(dane, k):
    return [row.copy() for row in dane if dobry(row, k)]


def zapisz_informacje(dane, sciezka):
    alergeny_num = [None for _ in range(len(dane))]
    for i in range(len(dane)):
        alergeny_num[i] = sum(dane[i])

    with open(sciezka, "w") as f:
        f.write(f"liczba dan: {len(dane)}\n")
        f.write(f"liczba uwzglednionych alergenow: {len(dane[0])}\n")

        f.write(f"maksymalna liczba alergenow w jednym daniu {max(alergeny_num)}\n")

        for i in range(max(alergeny_num) + 1):
            c = 0
            for j in range(len(alergeny_num)):
                if alergeny_num[j] == i:
                    c += 1
            f.write(f"liczba dan z {i} alergenami: {c}\n")


def main():
    dane = wczytaj_dane("alerg.csv")
    wypisz(dane)

    print("dania bez 0, 5, 10")
    print(szukaj_bezpiecznych_dan(dane, [0, 5, 10]))

    print("dodane nowe danie z alergenami 1, 2, 3, 8")
    dane = dodaj_nowe_danie(dane, [1, 2, 3, 8])
    wypisz(dane)

    print("dania po usunieciu tych z co najmniej 5 alergenami")
    dane = usun_najgorsze(dane, 5)
    wypisz(dane)

    zapisz_informacje(dane, "zapis.txt")


if __name__ == "__main__":
    main()
