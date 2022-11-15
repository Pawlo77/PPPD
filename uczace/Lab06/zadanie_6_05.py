import random
import matplotlib.pyplot as plt


def get_starting_perm(n):
    return list(range(n))


def generate_random_list(n):
    return [random.random() for _ in range(n)]


def swap(L, i1, i2):
    L[i1], L[i2] = L[i2], L[i1]


def selection_sort(L):
    perm = get_starting_perm(len(L))
    porow = przest = 0

    for i in range(len(L)):
        m = i

        for j in range(i + 1, len(L)):
            porow += 1
            if L[perm[j]] < L[perm[m]]:
                m = j

        if m != i:
            swap(perm, m, i)
            przest += 1

    return perm, porow, przest


def insertion_sort(L):
    perm = get_starting_perm(len(L))
    porow = przest = 0

    for i in range(1, len(L)):
        to_insert = perm[i]

        j = i
        while j > 0:
            porow += 1
            if L[perm[j - 1]] <= L[to_insert]:
                break

            przest += 1
            perm[j] = perm[j - 1]
            j -= 1

        if j != i:
            przest += 1
            perm[j] = to_insert

    return perm, porow, przest


def bubble_sort(L):
    perm = get_starting_perm(len(L))
    porow = przest = 0

    for i in range(len(L)):
        f = False

        for j in range(len(L) - 1 - i):
            porow += 1
            if L[perm[j]] > L[perm[j + 1]]:
                swap(perm, j, j + 1)
                przest += 1
                f = True

        if not f:
            break

    return perm, porow, przest


def binsearch(t, p, v):
    l = 0
    r = len(t) - 1

    while l <= r:
        mid = (l + r) // 2

        if t[p[mid]] == v:
            return p[mid]
        elif t[p[mid]] > v:
            r = mid - 1
        else:
            l = mid + 1

    return -1


def main():
    best = list(range(100))
    worst = best.copy()[::-1]

    algs = (
        ["Insertion Sort", insertion_sort, []],
        ["Bubble Sort", bubble_sort, []],
        ["Selection Sort", selection_sort, []],
    )

    ns = []
    for _ in range(5):
        n = random.randint(0, 200)
        ns.append(n)

        for j in range(100):
            L = generate_random_list(n)

            for i in range(len(algs)):
                if j == 0:
                    algs[i][2].append([0, 0])

                _, porow, przest = algs[i][1](L)

                # L1 = [L[x] for x in _]
                # assert L1 == sorted(L), "Zle posortowane"

                algs[i][2][-1][0] += porow
                algs[i][2][-1][1] += przest

    fig, (ax1, ax2) = plt.subplots(1, 2)

    for i in range(len(algs)):
        b = algs[i][1](best)
        w = algs[i][1](worst)

        print(algs[i][0])
        print("Najlepsze:", b[1], "porownan oraz", b[2], "przestawien.")
        print("Najgorsze:", w[1], "porownan oraz", w[2], "przestawien.")
        print("Srednie dla:")

        porownania = []
        przestawienia = []
        for j, (porow, przest) in enumerate(algs[i][2]):
            print(
                "\t", ns[j], "-", porow / n, "porownan oraz", przest / n, "przestawien."
            )
            porownania.append(porow / n)
            przestawienia.append(przest / n)

        ax1.scatter(ns, porownania, label=algs[i][0])
        ax2.scatter(ns, przestawienia)

        print()

    fig.legend()
    ax1.set_title("Porownania")
    ax2.set_title("Przestawienia")
    plt.show()


if __name__ == "__main__":
    main()

    L = [1, 2, 5, 1, 42, 14, 12]
    perm, _, _ = bubble_sort(L)
    print(binsearch(L, perm, 5))
