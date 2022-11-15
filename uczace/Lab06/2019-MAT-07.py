def get_next_row(row, n):
    next_row = [0 for _ in range(len(row) + 2)]

    next_row[0] = row[0]
    next_row[1] = row[0] + row[1]
    next_row[len(next_row) - 1] = row[len(row) - 1]
    next_row[len(next_row) - 2] = row[len(row) - 1] + row[len(row) - 2]

    for i in range(2, len(next_row) - 2):
        next_row[i] = row[i - 2] + row[i - 1] + row[i]
    return next_row


def TrinomialPlusInt(a, b, c, d, n):
    if n < 1:
        raise Exception("Zle n")
    if n == 1:
        return [a]
    elif n == 2:
        return [b, c, d]

    row = [b, c, d]
    for i in range(3, n + 1):
        row = get_next_row(row, i)
    return row


if __name__ == "__main__":
    print(TrinomialPlusInt(1, 2, 3, 4, 4))
    print(TrinomialPlusInt(1, 1, 1, 1, 5))
    # print(TrinomialPlusInt(1, 2, 3, 4, 0))
    print(TrinomialPlusInt(15, 5, 5, 5, 1))
    print(TrinomialPlusInt(15, 5, 6, 7, 2))
