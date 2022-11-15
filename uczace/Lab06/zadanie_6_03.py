import math


def pierwsza(k: int) -> list:
    P = [True if i % 2 != 0 else False for i in range(k + 1)]
    P[1] = False

    if k >= 2:
        P[2] = True

    z = math.ceil(math.sqrt(k)) + 1
    for i in range(3, z):
        for j in range(2 * i, k, i):
            P[j] = False

    return P


def plot(tab: list):
    print(" ", end="")  # to skip for 1

    for i in range(2, len(tab)):
        if tab[i]:
            print("o", end="")
        else:
            print(".", end="")

        if i % 10 == 0:
            print()

    if (len(tab) - 1) % 10 != 0:
        print()


if __name__ == "__main__":
    k = int(input("k: "))
    plot(pierwsza(k))
