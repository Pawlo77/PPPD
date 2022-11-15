import math
import random


def print_options():
    print("""
1 - polowanie
2 - tabela
3 - wyjście
    """)

def get_option():
    while True:
        opt = input("Wybierz co chcesz zrobic: ")

        if opt == "1":
            return 1
        elif opt == "2":
            return 2
        elif opt == "3":
            return 3
        
        print("Błędna opcja.")

def p_ataku(t, r):
    return 1 / (1 + math.exp(- 5 * t / ( 2 * r + 1)))

def polowanie(n_swoich, n_rywali, k):
    if n_swoich > n_rywali:
        return random.randint(30, 50)
    if n_swoich < n_rywali:
        return random.randint(5, 20)
    if n_swoich == n_rywali == 0:
        return k
    return 5

def wysyla(p):
    return random.choices([True, False], [p, 1 - p])[0]

def num_wilkow(w, s):
    z = 0
    if w:
        z = 1
    if s >= 2:
        z += 1
    return z
    # if w and s >= 2:
    #     print(2)
    #     return 2
    # if w:
    #     return 1
    return 0

def symulacja(p1, p2, n_dni, k):    
    s1 = s2 = 0
    z1 = z2 = 0

    for d in range(n_dni):
        w1 = wysyla(p1)
        w2 = wysyla(p2)

        wilki1 = num_wilkow(w1, s1)
        wilki2 = num_wilkow(w2, s2)

        # s1 = 0 if w1 != 0 else s1 + 1
        # s2 = 0 if w2 != 0 else s2 + 1
        s1 = 0 if wilki1 != 0 else s1 + 1
        s2 = 0 if wilki2 != 0 else s2 + 1

        z1 = (d * z1 + polowanie(wilki1, wilki2, k)) / (d + 1)
        z2 = (d * z2 + polowanie(wilki2, wilki1, k)) / (d + 1)

    return z1, z2

def tabela(r, k):
    best_s = 0
    best_p1 = best_p2 = None

    with open("wyniki.txt", "w") as f:
        for t1 in range(-r, r + 1):
            p1 = p_ataku(t1, r)
            row = f"p1={p1:.3f}:\t"

            for t2 in range(-r, r + 1):
                p2 = p_ataku(t2, r)

                z1, z2 = symulacja(p1, p2, 100, k)
                
                if z1 + z2 > best_s:
                    best_s = z1 + z2
                    best_p1, best_p2 = p1, p2

                row += f"({z1:.3f}, {z2:.3f}), "
            
            row = row[:-2] + "\n"
            f.write(row)

        print(f"Najlepsza suma to {best_s} dla p1 = {best_p1} i p2 = {best_p2}")


def main():
    while True:
        print_options()
        opt = get_option()

        if opt == 1:
            p1 = input("p1: ")
            p2 = input("p2: ")
            k = input("k: ")
            n_dni = input("n_dni: ")

            p1 = float(p1)
            p2 = float(p2)
            k = int(k)
            n_dni = int(n_dni)
            if not (0 <= p1 <= 1 and 0 <= p2 <= 1):
                raise ValueError("Niepoprawna wartosc")

            z1, z2 = symulacja(p1, p2, n_dni, k)
            print(f"Wynik symulacji to {z1:.3f} dla stada 1 oraz {z2:.3f} dla stada 2 [zajecy/dzien].")

        elif opt == 2:
            r = input("r: ")
            k = input("k: ")

            r = int(r)
            k = int(k)
            if r <= 0 or k <= 0:
                raise ValueError("Niepoprawne dane")

            tabela(r, k)

        else:
            print("Wyjscie")
            break


if __name__ == "__main__":
    random.seed(202121)
    main()