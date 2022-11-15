import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(123)


def moving_average(x: list, k: int) -> list:
    t = [float("NaN") for _ in range(len(x))]
    assert k % 2 == 1, "k musi byc nieparzyste"

    if k > len(x):
        return t
    l = (k - 1) // 2

    cur_sum = sum(x[:k])
    for i in range(l, len(x) - l):
        t[i] = cur_sum / k

        if i + l + 1 < len(x):
            cur_sum += x[i + l + 1] - x[i - l]

    return t


def main():
    n = 100  # liczba obserwacji
    s = 1  # odchylenie standardowe
    # x to skumulowana suma z obserwacji z rozkładu normalnego o wartości # oczekiwanej 0 i odchyleniu standardowym 1
    x = np.cumsum([random.normalvariate(0, s) for i in range(n)])

    # narysuj x[i] jako funkcja indeksów i=0,...,n-1
    plt.plot(x, color="black")
    # tutaj narysuj wygładzoną wersję x, wywołując moving_average i plt.plot...
    # użyj różnych kolorów dla różnych wartości parametru k

    for k in [3, 15, 31]:
        t = moving_average(x, k)
        plt.plot(t)

    plt.show()


if __name__ == "__main__":
    main()
