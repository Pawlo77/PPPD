def lr(x, y):
    x_hat = sum(x) / len(x)
    y_hat = sum(y) / len(y)

    beta_up = beta_down = 0.0
    for x_i, y_i in zip(x, y):
        beta_up += (x_i - x_hat) * (y_i - y_hat)
        beta_down += (x_i - x_hat) ** 2

    beta = beta_up / beta_down
    return beta, y_hat - beta * x_hat


def std(x):
    x_hat = sum(x) / len(x)

    res = 0.0
    for x_i in x:
        res += (x_i - x_hat) ** 2

    return math.sqrt(res / len(x))


def corr(x, y):
    x_hat = sum(x) / len(x)
    y_hat = sum(y) / len(y)
    s_x = std(x)
    s_y = std(y)

    sigma = 0.0
    for x_i, y_i in zip(x, y):
        sigma += ((x_i - x_hat) / s_x) * ((y_i - y_hat) / s_y)

    return 1 / (len(x) - 1) * sigma
