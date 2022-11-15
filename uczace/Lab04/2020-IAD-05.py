import random
import math

def skok():
    x = random.randint(0, 10)
    if x < 5:
        return 1
    elif 5 <= x <= 7:
        return 2
    return 3

def mega_skok():
    x = random.randint(0, 10)
    if x < 3:
        return 5
    return -1

def atak(k1, k2):
    if k1 <= k2:
        return k1, k2

    x = random.randint(0, 2)
    if x == 0:
        k2 = max(k2 - math.ceil((k1 - k2) ** 2 / 4), 0)
    else:
        k1 = max(k1 - 1, 0)
    return k1, k2

def opcja(k):
    print(f"""
--- Ruch kozicy {k} ---
1 - skok
2 - mega skok
3 - atak
    """)

def ruch(name):
    while True:
        opt = input(f"Ruch kozy {name}: ")

        if opt == "1":
            return 1
        elif opt == "2":
            return 2
        elif opt == "3":
            return 3
        
        print("Błędna opcja")

def koniec(k1, k2):
    if k1 >= 20 and k2 >= 20:
        if k1 > k2:
            print("Wygrała koza 1")
        elif k1 < k2:
            print("Wygrała koza 2")
        else:
            print("Remis")
    elif k1 >= 20:
        print("Wygrała koza 1")
    elif k2 >= 20:
        print("Wygrała koza 2")
    else:
        return False
    return True

def make_move(k1, k2, move, id):
    global f
    msg = "Kozica {} - wybor {}, ruch: {}\n"

    if move == 1:
        s = skok()
        f.write(msg.format(id, "skok", s))
        k1 += s
    elif move == 2:
        s = mega_skok()
        f.write(msg.format(id, "mega_skok", s))
        k1 = max(s + k1, 0)
    else:
        s1, s2 = atak(k1, k2)
        f.write(msg.format(id, "atak", f"kozica atakowana - {s2 - k2}, kozica atakująca - {s1 - k1}"))
        k1, k2 = s1, s2

    return k1, k2

def status(k1, k2):
    global f
    msg = "Pozycja kozicy {} - {}.\n"
    f.write(msg.format(1, k1))
    f.write(msg.format(2, k2))
    print(msg.format(1, k1))
    print(msg.format(2, k2))


def main():
    k = k1 = k2 = 0
    global f
    f = open("kozica.txt", "w")

    while True:
        opcja(1)
        opt1 = ruch(1)
        k1, k2 = make_move(k1, k2, opt1, 1)
        
        status(k1, k2)
        if koniec(k1, k2):
            break

        opcja(2)
        opt2 = ruch(2)
        k2, k1 = make_move(k2, k1, opt2, 2)
    
        status(k1, k2)
        if koniec(k1, k2):
            break
    f.close()


if __name__ == "__main__":
    main()