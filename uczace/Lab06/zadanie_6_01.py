import math
import random
import matplotlib.pyplot as plt


def regresja(x: list, y: list) -> list:
    assert len(x) == len(y)

    x_hat = sum(x) / len(x)
    y_hat = sum(y) / len(y)

    up = down = 0
    for x_i, y_i in zip(x, y):
        up += (x_i - x_hat) * (y_i - y_hat)
        down += (x_i - x_hat) ** 2
    beta = up / down

    alpha = y_hat - beta * x_hat

    return alpha, beta


def E(alpha: float, beta: float, x: list, y: list) -> float:
    res = 0.0

    for x_i, y_i in zip(x, y):
        res += (alpha + beta * x_i - y_i) ** 2
    return res


def std(x: list) -> float:
    res = 0.0

    x_hat = sum(x) / len(x)
    for x_i in x:
        res += (x_i - x_hat) ** 2

    return math.sqrt(res / (len(x) - 1))


def r(x: list, y: list) -> float:
    res = 0.0

    x_hat = sum(x) / len(x)
    y_hat = sum(y) / len(y)
    s_x = std(x)
    s_y = std(y)

    for x_i, y_i in zip(x, y):
        res += ((x_i - x_hat) / s_x) * ((y_i - y_hat) / s_y)

    return 1 / (len(x) - 1) * res


def main():
    random.seed(123)
    N = 100

    alpha0 = -3
    beta0 = 1.5
    x = [random.uniform(-10, 10) for i in range(N)]
    y = [alpha0 + beta0 * x[i] + random.normalvariate(0, 1) for i in range(N)]

    alpha, beta = regresja(x, y)
    e = E(alpha, beta, x, y)

    e_min = float("inf")
    alpha_min = beta_min = None
    for _ in range(N):
        alpha_temp = random.random()
        beta_temp = random.random()

        e_temp = E(alpha_temp, beta_temp, x, y)

        if e_temp < e_min:
            e_min = e_temp
            alpha_min, beta_min = alpha_temp, beta_temp

    cor = r(x, y)

    print(f"E for best fit - {e:5.3f}. Best E out of {N} random fits - {e_min:5.3f}")
    print(f"Wspl korelacji - {cor:5.5f}")

    plt.scatter(x, y)
    plt.plot([-10, 10], [alpha0 + beta0 * -10, alpha0 + beta0 * 10], "g--")
    plt.plot([-10, 10], [alpha + beta * -10, alpha + beta * 10], "r-")
    plt.plot([-10, 10], [alpha_min + beta_min * -10, alpha_min + beta_min * 10], "b--")
    plt.axis([-10, 10, -10, 10])
    plt.show()


if __name__ == "__main__":
    main()
