def get_starting_perm(n):
    return list(range(n))


def swap(L, i1, i2):
    L[i1], L[i2] = L[i2], L[i1]


def selection_sort(L):
    perm = get_starting_perm(len(L))

    for i in range(len(L)):
        m = i

        for j in range(i + 1, len(L)):
            if L[perm[j]] < L[perm[m]]:
                m = j

        if m != i:
            swap(perm, m, i)

    return perm


def insertion_sort(L):
    perm = get_starting_perm(len(L))

    for i in range(1, len(L)):
        to_insert = perm[i]

        j = i
        while j > 0:
            if L[perm[j - 1]] <= L[to_insert]:
                break

            perm[j] = perm[j - 1]
            j -= 1

        if j != i:
            perm[j] = to_insert

    return perm


def bubble_sort(L):
    perm = get_starting_perm(len(L))

    for i in range(len(L)):
        f = False

        for j in range(len(L) - 1 - i):
            if L[perm[j]] > L[perm[j + 1]]:
                swap(perm, j, j + 1)
                f = True

        if not f:
            break

    return perm


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
