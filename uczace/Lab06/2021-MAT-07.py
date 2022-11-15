# funkcja wczytujaca dane; na wejsciu dostaje nazwe pliku; na wyjsciu zwraca liste wczytanych elementow
def read_data(datafile):
    extracted_data = [i.strip().split() for i in open(datafile)]
    flat_list = [int(item) for sublist in extracted_data for item in sublist]
    return flat_list


def validate(d, n, koords):
    d, n = int(d), int(n)
    assert d < n, "d musi byc mniejsze od n"
    assert max(koords) < n, "koordynaty nie moga wykraczac poza n-1"


def merge_islands(koords):
    if len(koords) <= 2:
        return koords

    l, r = 0, 1
    i = 2
    while i + 1 < len(koords):
        if koords[r] >= koords[i]:
            koords[r] = max(koords[r], koords[i + 1])
            del koords[i]  # i th element
            del koords[i]  # i + 1 th element (ith deleted so index is lowered by one)
        else:
            l = i
            r = i + 1
            i += 2

    return koords


def create_map(koords, n, d):
    mapa = ["_" for _ in range(n)]

    if len(koords) == 0:
        return mapa

    island_r, island_l = -d - 1, 0
    for i in range(n):
        print(island_r, island_l, i, koords)
        if island_l is not None and koords[island_l] <= i <= koords[island_l + 1]:
            mapa[i] = "|"
        elif koords[island_r] + d >= i or (
            island_l is not None and i + d >= koords[island_l]
        ):
            print(koords[island_r] + d >= i)
            print(island_l is not None and i + d <= koords[island_l])
            mapa[i] = "-"

        if island_l is not None and i >= koords[island_l + 1]:
            island_r = min(island_l + 1, len(koords) - 1)
            island_l += 2

            if not island_l < len(koords):
                island_l = None

    return mapa


def main():
    koords = read_data("2021-MAT-07_koordynaty_wysp.csv")
    d = input("d: ")
    n = input("n: ")
    validate(d, n, koords)

    koords = merge_islands(koords)
    print(create_map(koords, n, d))


if __name__ == "__main__":
    main()
