import csv


def load():
    studenci = []
    with open("studenci.csv") as f:
        for row in csv.reader(f):
            studenci.append(row)
    return studenci


def popraw(studenci):
    for i in range(len(studenci)):
        studenci[i][2] = int(studenci[i][2])  # id

        s = 0
        missing_count = 0
        for j in range(3, len(studenci[i])):
            if studenci[i][j] != "":
                studenci[i][j] = float(studenci[i][j])
                s += studenci[i][j]
            else:
                missing_count += 1

        s /= len(studenci[i]) - 3 - missing_count
        if missing_count > 0:
            if missing_count == 2:
                s = 0.0

            for j in range(3, len(studenci[i])):
                if studenci[i][j] == "":
                    studenci[i][j] = s

        if len(studenci[i]) == 9:
            student = [studenci[i][j] for j in range(8)]
            studenci[i] = student


def print_list(X):
    for row in X:
        print("|", end="")

        for val in row:
            if not isinstance(val, float):
                print(f"{val:^12}", end="")
            else:
                print(f"{val:^8.1f}", end="")

        print("|")


def ocena(student):
    s = 0
    for i in range(3, len(student)):
        s += student[i]
    s /= 20.0 * (len(student) - 3)

    if s >= 0.91:
        return 5.0
    if s >= 0.81:
        return 4.5
    if s >= 0.71:
        return 4.0
    if s >= 0.61:
        return 3.5
    if s >= 0.51:
        return 3.0
    return 2.0


def oceny(studenci):
    return [[student[2], ocena(student)] for student in studenci]


def statystyki(studenci):
    res = [None for _ in range(len(studenci[0]) - 3)]

    for j in range(3, len(studenci[0])):
        nr_zad = j - 2
        max_score = -float("inf")
        min_score = float("inf")
        avg_score = 0.0

        for student in studenci:
            score = student[j]

            if score > max_score:
                max_score = score
            if score < min_score:
                min_score = score
            avg_score += score

        avg_score /= len(studenci)
        res[j - 3] = [nr_zad, max_score, min_score, avg_score]

    return res


def main():
    studenci = load()
    popraw(studenci)
    print_list(studenci)

    o = oceny(studenci)
    print_list(o)

    stats = statystyki(studenci)
    print_list(stats)


if __name__ == "__main__":
    main()
