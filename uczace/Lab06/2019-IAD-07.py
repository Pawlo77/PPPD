def podaj():
    max_el = int(input("Podaj najwiekszy element do przechowania: "))
    Z = [0 for _ in range(max_el + 1)]

    for i in range(max_el + 1):
        el = int(input(f"Z[{i}] = "))

        if el < 0:
            raise Exception(f"Nie da się przechować ujemnej ilości {i}.")

        Z[i] = el

    if Z[max_el] == 0:
        raise Exception("Ostatni element multizbioru musi być dodatni")

    return Z


def wypisz(Z):
    print("[", end="")
    for i, el in enumerate(Z):
        print(f"{i}, " * el, end="")
    print("]")


def dodaj(zbior, element):
    if element >= len(zbior):
        Z = [0 for _ in range(element + 1)]
        Z[element] = 1

        for i, el in enumerate(zbior):
            Z[i] += el
        return Z

    zbior[element] += 1
    return zbior


def przeciecie(zbiorA, zbiorB):
    len_ = min(len(zbiorA), len(zbiorB))
    P = [0 for _ in range(len_)]

    for i in range(len_):
        P[i] = min(zbiorA[i], zbiorB[i])
    return P


def roznica(zbiorA, zbiorB):
    len_ = min(len(zbiorA), len(zbiorB))
    R = [0 for _ in range(len(zbiorA))]

    last_non_zero = None
    for i in range(len_):
        R[i] = max(zbiorA[i] - zbiorB[i], 0)

        if R[i] > 0:
            last_non_zero = i

    for i in range(len_, len(zbiorA)):
        R[i] = zbiorA[i]
        last_non_zero = i

    if last_non_zero + 1 != len(R):
        return [R[i] for i in range(last_non_zero + 1)]
    return R


def main():
    Z = podaj()

    print()
    wypisz(Z)

    print()
    el = int(input("Podaj nowy element: "))
    Z = dodaj(Z, el)

    print()
    wypisz(Z)

    print()
    Z2 = podaj()

    print()
    print("Roznica zbiorow 1 i 2")
    R = roznica(Z, Z2)
    wypisz(R)

    print()
    P = przeciecie(Z, Z2)
    print("Przeciecie zbiorow 1 i 2")
    wypisz(P)


if __name__ == "__main__":
    main()
