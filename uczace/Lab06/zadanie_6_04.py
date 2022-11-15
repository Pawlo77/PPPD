import random


# https://en.wikipedia.org/wiki/Reservoir_sampling
# Algorithm R
def comb(k: int) -> list:
    res = [None] * k

    for i in range(k):
        res[i] = int(input())

        if res[i] < 0:
            raise ValueError("k < n nie spelnione")

    num = k
    x = int(input())

    while x >= 0:
        num += 1
        j = random.randrange(0, num)

        if j < k:
            res[j] = x
        x = int(input())

    return res


if __name__ == "__main__":
    random.seed(42)

    k = int(input("k: "))
    print(comb(k))
