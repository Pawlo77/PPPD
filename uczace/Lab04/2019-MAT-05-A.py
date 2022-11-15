import random

def mozliwe_akcje():
    print("""
1   Atak toporem
2   Magiczny pocisk
3   Potezny atak
4   Zapisz gre
5   Odczytaj gre
    """)

def wypisz_zycie_trolla(hp_troll):
    print(f"Troll ma {hp_troll} hp.")

def pobierz_akcje(mana, tury_od_p):
    while True:
        akcja = input("Twoja akcja: ")

        if akcja == "1":
            return 1
        elif akcja == "2":
            if mana >= 20:
                return 2
            else:
                print("Brak many.")
        elif akcja == "3":
            if tury_od_p >= 3:
                return 3
            else:
                print("Uzyles go niedawno")
        elif akcja in ["4", "5"]:
            return int(akcja)
        else:
            print("Niepoprawna liczba")

def zapisz_gre(hp_troll, mana, tury_od_p):
    sciezka = input("Podaj sciezke gdzie zapisac gre: ")
    with open(sciezka, "w") as f:
        for param in [hp_troll, mana, tury_od_p]:
            f.write(str(param) + "\n")

def odczytaj_gre():
    sciezka = input("Podaj sciezke gdzie zapisano gre: ")
    with open(sciezka, "r") as f:
        hp_troll, mana, tury_od_p = f.readlines()

    return (int(hp_troll), int(mana), int(tury_od_p))


def main():
    hp_troll = 1000
    hp_zyg = 100
    ataki = 0
    tury_od_p = 3
    mana = 40

    while hp_troll > 0:
        wypisz_zycie_trolla(hp_troll)
        mozliwe_akcje()
        a = pobierz_akcje(mana, tury_od_p)

        if a == 1:
            ataki += 1

            if random.choice(list(range(10))) in [0, 1, 2]:
                hp_troll -= 230
        elif a == 2:
            ataki += 1
            mana -= 20
            hp_troll -= random.randint(50, 100)
        elif a == 3:
            tury_od_p = 0
            ataki += 1
            if random.randint(0, 99) < 35:
                hp_troll -= random.randint(200, 400)
        elif a == 4:
            zapisz_gre(hp_troll, mana, tury_od_p)
        elif a == 5:
            hp_troll, mana, tury_od_p = odczytaj_gre()
        else:
            tury_od_p += 1

if __name__ == '__main__':
    main()