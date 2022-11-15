import random
import math
import copy


def wygeneruj_prosta_sciezke(n):
    """
    Zwraca n-elementową listę o wartościach [0,1,2,3,...,n-1]
    :param n: długość listy
    :return: lista
    """
    return list(range(n))


def wygeneruj_miasta_A(n, min_x=-10, max_x=10, min_y=-10, max_y=10):
    """
    Generuje dwie listy (jedna ma współrzędne x, a druga współrzędne y) reprezentujące współrzędne miast.
    Współrzędne miast są losowane z rozkładu jednostajnego U[min_x, max_x] dla współrzędnych x oraz U[min_y, max_y]
    dla współrzędnych y.
    :param n: liczba miast
    :param min_x: minimalna współrzędna x
    :param max_x: maksymalna współrzędna x
    :param min_y: minimalna współrzędna y
    :param max_y: maksymalna współrzędna y
    :return: dwuelementowa krotka, gdzie pierwszy element jest n-elementową listą współrzędnych x,
    a drugi element n-elementową listą współrzędnych y
    """
    X = [None for _ in range(n)]
    Y = [None for _ in range(n)]

    i = 0
    while i < n:
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)

        good = True
        for j in range(i):
            if X[j] == x and Y[j] == y:
                good = False
                break

        if good:
            X[i] = x
            Y[i] = y
            i += 1

    return X, Y


def dist(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka):
    """
    Dla zadanej listy indeksów miast oblicz długość cyklu. Wyjaśnijmy: pomimo nazwy parametru "sciezka" mamy na myśli
    cykl: z ostatniego miasta przechodzimy z powrotem do pierwszego (zerowego).
    :param miasta_x: lista współrzędnych x-owych miast
    :param miasta_y: lista współrzędnych y-owych miast
    :param sciezka: lista indeksów miast, zgodnie z którą przemieszczamy się od miasta do miasta. Z ostatniego miasta
    przechodzimy z powrotem do pierwszego (zerowego).
    :return: pojedyncza liczba typu float oznaczająca długość cyklu
    """
    dl = 0

    n = 1
    while n < len(sciezka):
        dl += dist(
            miasta_x[sciezka[n]],
            miasta_x[sciezka[n - 1]],
            miasta_y[sciezka[n]],
            miasta_y[sciezka[n - 1]],
        )
        n += 1

    dl += dist(
        miasta_x[sciezka[0]],
        miasta_x[sciezka[len(sciezka) - 1]],
        miasta_y[sciezka[0]],
        miasta_y[sciezka[len(sciezka) - 1]],
    )

    return dl


def mutuj_A(sciezka, k=3):
    """
    Funkcja mutuje podaną listę indeksów. Funkcja nie modyfikuje argumentów wejściowych. Funkcja zwraca zmodyfikowaną kopię.
    Funkcja działa w sposób następujący: losowane jest k indeksów listy bez zwracania. Następnie geny są przesuwane cyklicznie
    po wylosowanych indeksach. Przykładowo, jeśli lista to [1,11,2,3,22,4,5,33], a wylosowane indeksy to [1,4,7] (dwucyfrowe elementy
    z listy) to wynikowa ścieżka powinna być równa [1,22,2,3,33,4,5,11].

    Można (należy) użyć random.sample().

    :param sciezka: Lista indeksów, którą należy zmutować.
    :param k: Liczba indeksów do wylosowania (domyślnie równy 3)
    :return: Zmutowana kopia ścieżki
    """
    S = sciezka.copy()
    idxs = random.sample(list(range(len(S))), k)
    temp = None

    for idx in range(len(idxs) - 1, -1, -1):
        if temp is None:
            temp = S[idxs[idx]]
        else:
            S[idxs[idx]], temp = temp, S[idxs[idx]]
    S[idxs[len(idxs) - 1]] = temp

    return S


def krzyzuj_A(sciezka1, sciezka2):
    """
    Funkcja dokonuje krzyżowania dwóch ścieżek. Krzyżowanie polega na wylosowaniu pewnego indeksu z zakresu {1, 2,..., n-2}
    (gdzie n to długość jednej ścieżki), a następnie przepisanie elementów ze ścieżki 1 do dziecka od zera do wylosowanego indeksu.
    Reszta indeksów miast powinna zostać wpisana w pozostałe miejsca zgodnie z kolejnością występowania na sciezka2.

    Przykładowo, jeśli sciezka1=[0,1,2,3,4,5,6], a sciezka2=[6,5,4,3,2,1,0], a wylosowany index=3, to dziecko powinno mieć
    postać [0,1,2,6,5,4,3].

    :param sciezka1: lista indeksów miast
    :param sciezka2: lista indeksów miast
    :return: lista indeksów miast
    """
    idx = random.randint(1, len(sciezka1) - 2)
    D = [0 for _ in range(len(sciezka1))]

    i = 0
    while i < idx:
        D[i] = sciezka1[i]
        i += 1

    i2 = 0
    while i < len(sciezka1):

        i3 = 0
        while i3 < i:
            if D[i3] == sciezka2[i2]:
                break
            i3 += 1

        if i3 == i:
            D[i] = sciezka2[i2]
            i += 1
        i2 += 1

    return D


def swap(A, i0, i1):
    A[i0], A[i1] = A[i1], A[i0]


def znajdz_rozwiazanie_optymalne_A(miasta_x, miasta_y):
    """
    Znajduje rozwiązanie optymalne problemu komiwojażera poprzez rozpatrzenie wszystkich permutacji miast.
    :param miasta_x: lista współrzędnych x-owych miast
    :param miasta_y: lista współrzędnych y-owych miast
    :return: krotka, której pierwszym elementem jest optymalna długość cyklu, a drugim optymalna lista indeksów miast
    """
    C = [0 for _ in range(len(miasta_x))]
    road = wygeneruj_prosta_sciezke(len(miasta_x))

    best_dist = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, road)
    best_set = road

    i = 0
    while i < len(road):
        if C[i] < i:
            if i % 2 == 0:
                swap(road, 0, i)
            else:
                swap(road, C[i], i)

            dist = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, road)
            if dist < best_dist:
                best_dist = dist
                best_set = road.copy()

            C[i] += 1
            i = 0
        else:
            C[i] = 0
            i += 1

    return best_dist, best_set


def main_A():
    random.seed(123)
    n = 7
    min_x, max_x, min_y, max_y = -5, 4, -4, 5
    # grupa A
    # etap 1
    print("0. Generujemy miasta")
    miasta_x, miasta_y = wygeneruj_miasta_A(n, min_x, max_x, min_y, max_y)
    print(miasta_x)
    print(miasta_y)

    print("\n\n1. Szukamy prostą mutacją")
    sciezka = wygeneruj_prosta_sciezke(n)
    print(f"Prosta sciezka: {sciezka}")
    best_sciezka = sciezka
    best_wartosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka)
    print(f"Dla prostej ścieżki długość ścieżki to: {best_wartosc}")

    print(f"mutuj_A([0,1,2,3,4,5,6], 3) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 3)}")
    print(f"mutuj_A([0,1,2,3,4,5,6], 4) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 4)}")
    print(f"mutuj_A([0,1,2,3,4,5,6], 5) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 5)}")

    # [TO UZUPELNIJ]
    # 100 razy wykonaj:
    # mutację aktualnie najlepszej ścieżki
    # sprawdzenie, czy zmutowana ścieżka daje krótszy (lepszy) cykl
    # jeśli tak, zapisz lepszy wynik w zmiennych best_sciezka, best_wartosc
    for _ in range(100):
        sciezka = mutuj_A(best_sciezka)
        wartosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka)

        if wartosc < best_wartosc:
            best_wartosc = wartosc
            best_sciezka = sciezka

    print(f"Po mutacjach długość ścieżki {best_sciezka} to: {best_wartosc}")

    print("\n\n2. Szukamy przez krzyzowanie")

    sciezka1 = mutuj_A(wygeneruj_prosta_sciezke(n), n - 2)
    sciezka2 = mutuj_A(wygeneruj_prosta_sciezke(n), n - 2)
    wartosc1 = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka1)
    wartosc2 = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka2)

    # [TO UZUPELNIJ]
    # Nasza populacja składa się ze sciezka1 i sciezka2
    # Powtórz 1000 razy:
    # skrzyżuj ścieżkę1 i ścieżkę2
    # oblicz długość cyklu dla dziecka
    # pozostaw w zmiennych sciezka1, wartosc1 i sciezka2, wartosc2 wartosci odpowiadajace dwóm najlepszym wynikom z trzech możliwych (sciezka1, sciezka2, dziecko)
    # Podpowiedz: uzyj mechanizmu jak przy sortowaniu przez wstawianie.

    for _ in range(1000):
        dziecko = krzyzuj_A(sciezka1, sciezka2)
        wartosc_d = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, dziecko)
        temp = sorted(
            [(wartosc1, sciezka1), (wartosc2, sciezka2), (wartosc_d, dziecko)],
            key=lambda x: x[0],
        )

        wartosc1, sciezka1 = temp[0]
        wartosc2, sciezka2 = temp[1]

    print(f"\n\nPo krzyżowaniu długość ścieżki {sciezka1} to: {wartosc1}")

    # etap 5:

    optymalne = znajdz_rozwiazanie_optymalne_A(miasta_x, miasta_y)
    print(f"\n\n3. Optymalny wynik to {optymalne}")


if __name__ == "__main__":
    main_A()
