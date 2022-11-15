import random


def losuj_litery(dlugosc: int) -> list:
    return [chr(random.randint(ord("a"), ord("z"))) for _ in range(dlugosc)]


def polacz_z_zawijaniem(pierwsza: list, druga: list) -> list:
    n = 2 * len(pierwsza) if len(pierwsza) > len(druga) else 2 * len(druga)
    res = [None for _ in range(n)]

    p = l = i = 0
    while i < n / 2:
        res[i] = pierwsza[p]
        i += 1
        p = (p + 1) % len(pierwsza)
    while i < len(res):
        res[i] = druga[l]
        i += 1
        l = (l + 1) % len(druga)

    return res


def odwroc(lista: list, l: int, r: int) -> list:
    zakres = r - l + 1
    if zakres % 2 == 1:
        zakres -= 1

    for i in range(zakres // 2):
        lista[l + i], lista[r - i] = lista[r - i], lista[l + i]
    return lista


def przesun_w_lewo(lista: list, ile: int) -> None:
    i = 0
    temp = lista[i]

    for _ in range(len(lista)):
        new_i = i - ile
        if new_i < 0:
            new_i = len(lista) + new_i
        i = new_i

        lista[new_i], temp = temp, lista[new_i]


def mod_26(tab: list) -> None:
    t0 = t1 = t2 = 0

    for i in range(len(tab)):
        t1 = ord(tab[i])
        t2 = 0 if i + 1 >= len(tab) else ord(tab[i + 1])

        tab[i] = chr(ord("a") + (t0 + t1 + t2) % 26)
        t0 = t1


def main():
    random.seed(2014)

    dlugosc = int(input("Podaj liczbę z zakresu <5, 15>: "))
    if not 5 <= dlugosc <= 15:
        raise ValueError("Błędna dlugosc")

    print(f"Losuj litery: {dlugosc}")
    L1 = losuj_litery(dlugosc)
    print(L1)
    print()

    print(f"Losuj litery: {dlugosc * 2 + 1}")
    L2 = losuj_litery(dlugosc * 2 + 1)
    print(L2)
    print()

    print("Polacz z zwijaniem")
    L3 = polacz_z_zawijaniem(L1, L2)
    print(L3)
    print()

    l, r = 3, 7
    print(f"Odwroc 2 pomiedzy {l} a {r}")
    print(L2)
    print(odwroc(L2, l, r))
    print()

    n = 3
    print(f"Przesun w lewo 1 o {n}")
    print(L1)
    przesun_w_lewo(L1, n)
    print(L1)
    print()

    print("Mod 26 na L1")
    print(L1)
    mod_26(L1)
    print(L1)


if __name__ == "__main__":
    main()
