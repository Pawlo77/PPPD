import random


def rzucaj(l):
    return [random.randint(1, 6) for _ in range(l)]


def sprawdz(rzuty, n):
    prev_rzut = None
    pos = 0

    i = 0
    while i < len(rzuty):
        git

        if rzut % 2 == 0:
            pos += rzut

        elif prev_rzut is not None and prev_rzut % 2 == 1:
            prev_rzut = 0
            i += 1
            continue

        else:
            pos -= rzut

        prev_rzut = rzut
        i += 1

    if pos >= n:
        return True, pos
    return False, pos


def symuluj(L, n, p):
    positions = [None for _ in range(p)]
    statuses = [None for _ in range(p)]

    for i in range(p):
        rzuty = rzucaj(L[i])
        status, pos = sprawdz(rzuty, n)

        positions[i] = pos
        statuses[i] = status

        print(f"Próba nr {i + 1}.")
        print(f"Rzuty: {rzuty}")
        print(
            f"Wykonując {L[i]} rzutow udalo sie pokonac {pos} krokow. Do pokonania pozostalo {max(n - pos, 0)} krokow"
        )

    return positions, statuses


if __name__ == "__main__":
    random.seed(9876)

    n = 30
    p = 12
    L = [random.randrange(12, 40, 2) for _ in range(p)]

    positions, statuses = symuluj(L, n, p)

    print(f"Kroki pokonane we wszystkich probach: {positions}")
    print(f"Sukces kazdej z grup: {statuses}")
