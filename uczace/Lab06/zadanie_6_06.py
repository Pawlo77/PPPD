import random


def how_many(w):
    can_see = [True for _ in range(len(w))]
    for i in range(1, len(w)):
        delta = (w[i] - w[0]) / i

        for j in range(1, i):
            if w[j] > w[0] + j * delta:
                can_see[i] = False
                break

    return can_see[1:]


def height(w):
    max_delta = 0

    for i in range(1, len(w)):
        for j in range(i):
            delta = j * (w[j] - w[i]) / (i - j) + w[j]

            if delta > max_delta:
                max_delta = delta
    return max_delta


def main():
    # n = int(input("Podaj liczbe wiezowcow: "))
    n = 5
    assert n > 0, "Liczba wiezowcow musi byc nieujemna"

    # w = [int(x) for x in input("Podaj wysokosci wiezowcow: ").split()]
    w = [40, 30, 10, 50, 40]
    assert min(w) > 0, "wysokosc wiezowcow musi byc nieujemna"
    assert len(w) == n, f"nie podales dokladnie {n} wiezowcow"

    largest = [(w[0], 0)]
    for i in range(1, len(w)):
        if w[i] > largest[-1][0]:
            largest.append((w[i], i))
        else:
            largest.append(largest[-1])

    print(f"Pierwszy snajper widzi {sum(how_many(w))} snajperow")
    print(f"Najmniejsza wysokość I wiezowca gwarantująca sukces: {height(w)}")

    # brute force test for height() algorithm
    # for _ in range(1000):
    #     w = [random.randint(1, 400) for _ in range(random.randint(50, 500))]
    #     h = height(w)

    #     w[0] = h
    #     assert len(w) - 1 == sum(how_many(w))

    #     w[0] -= 1
    #     assert len(w) - 1 > sum(how_many(w))


if __name__ == "__main__":
    main()
