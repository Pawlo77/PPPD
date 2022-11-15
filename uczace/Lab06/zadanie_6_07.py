import math


def main():
    schody = int(input("Podaj liczbe schodkow: "))
    assert schody > 0, "Badamy dla dodatniej liczby schodkow"

    S = input("Podaj wysokosci schodkow (w cm, oddzielone spacja): ")
    S = [0] + [int(x) for x in S.split(" ")]
    assert min(S[1:]) > 0, "Schodki musza miec dodatnia wysokosc"

    skoki = 0
    maks_diff = 0
    maks_diff_schodek = None
    for i in range(1, len(S)):
        diff = S[i - 1] / 2 + S[i]

        if diff > 100:
            break
        elif diff > maks_diff:
            maks_diff = diff
            maks_diff_schodek = i
        skoki += 1

    print(f"Skoczek pokona {skoki} skokow")
    if skoki == len(S) - 1:
        print(
            f"Najmniejsza wysokosc schodka 0 to {min(101, math.ceil((100.01 - maks_diff) * 2 ** (maks_diff_schodek - 1) + S[1]))}"
        )


if __name__ == "__main__":
    main()
