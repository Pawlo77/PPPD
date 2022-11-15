import random
import math


def print_header():
    print("""
1 - wylosuj początek przedziału
2 - wylosuj koniec przedziału
3 - Zapisz wyliczenia do pliku
4 - wczytaj stan z pliku
5 - wyjdź z programu
    """)

def read_action():
    while True:
        a = input("Wybierz akcję: ")

        for i in range(1, 6):
            try:
                a = int(a)
            except:
                break
            else:
                if a == i:
                    return i
        print("Błędna akcja.")
        print_header()

def generate_beginning(order_of_magnitude):
    r = 0
    for _ in range(order_of_magnitude):
        r = 10 * r + random.randint(1, 6)
    return r

def generate_end(order_of_magnitude):
    weights = [.1] * 10
    weights[0] = 0.15
    weights[-1] = 0.05

    r = 0
    choices = random.choices(list(range(10)), weights=weights, k=order_of_magnitude)
    for choice in choices:
        r = 10 * r + choice
    return r

def is_abundant(x):
    r = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            r += i
    return r > x

def concatenate_abundants_from_range(l, p):
    if math.isnan(l) or math.isnan(p):
        return math.nan

    r = 0
    for i in range(l, p + 1):
        if is_abundant(i):
            k = 1
            while i > k:
                k *= 10
            r = k * r + i
    return r

def save_file(l, r, contatenation, order_of_magnitude):
    if math.isnan(l) or math.isnan(r):
        print("Wymagane dane nie są wypełnione")
    else:
        path = input("Gdzie zapisac? ")
        with open(path, "w") as f:
            print(l, r, contatenation, order_of_magnitude, file=f, sep=";")

def read_from_file():
    path = input("Skąd wczytać? ")
    with open(path, "r") as f:
        return (int(x) for x in f.readline().strip().split(";"))

def print_state(l, r, contatenation):
    print(f"<{l} : {r}> => {contatenation}")

def main():
    order_of_magnitude = 1 if random.randint(0, 9) < 6 else 2
    print(f"Początek przedziału będzie {order_of_magnitude}-cyfrowy")

    l = r = math.nan
    contatenation = math.nan
    while True:
        print_header()
        action = read_action()

        if action == 1:
            l = generate_beginning(order_of_magnitude)
        elif action == 2:
            r = generate_end(order_of_magnitude + 1)
        elif action == 3:
            save_file(l, r, order_of_magnitude, contatenation)
        elif action == 4:
            l, r, contatenation, order_of_magnitude = read_from_file()
        else:
            print("Wyjście")
            break

        contatenation = concatenate_abundants_from_range(l, r)
        print_state(l, r, contatenation)


if __name__ == "__main__":
    random.seed(2014)
    main()