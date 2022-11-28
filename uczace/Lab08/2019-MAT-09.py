import csv


def wczytaj_csv():
    uczestnicy = []
    with open("wyniki_ankiety.csv") as f:
        for row in csv.reader(f):
            uczestnicy.append(row)
    return uczestnicy


def zlicz_odpowiedzi(macierz):
    res = [[None for _ in range(len(macierz[0]) - 3)] for _ in range(3)]

    for j in range(3, 8):
        tak = nie = b = 0

        for wynik in macierz:
            if wynik[j] == "tak":
                tak += 1
            elif wynik[j] == "nie":
                nie += 1
            else:
                b += 1

        res[0][j - 3] = tak
        res[1][j - 3] = nie
        res[2][j - 3] = b

    return res


def narysuj_tabelę(zliczenie):
    header = " " * 12 + "TAK NIE  B/O  "
    print(zliczenie)
    print(header)

    print("-" * len(header))
    for j in range(len(zliczenie[0])):
        print(
            f"{f'Pytanie{j}':<12s}{zliczenie[0][j]:<5d}{zliczenie[1][j]:<5d}{zliczenie[2][j]:<5d}"
        )
        print("-" * len(header))


def statystyki(macierz):
    l_kob = l_men = 0
    s_wieku = 0.0
    n_wiek_not_nan = 0

    for row in macierz:
        if row[1] == "k":
            l_kob += 1
        elif row[1] == "m":
            l_men += 1

        if row[2] != "":
            n_wiek_not_nan += 1
            s_wieku += float(row[2])

    s_wieku /= n_wiek_not_nan

    print()
    print("Liczba ankietowanych:", len(macierz))
    print("Średnia wieku:", round(s_wieku, 1))
    print("Liczba kobiet:", l_kob)
    print("Liczba mężczyzn:", l_men)


def main():
    ankieta = wczytaj_csv()
    zliczenie = zlicz_odpowiedzi(ankieta)
    narysuj_tabelę(zliczenie)
    statystyki(ankieta)


if __name__ == "__main__":
    main()
