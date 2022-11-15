def main():
    n = int(input("Podaj n: "))
    assert n > 6, "Bledne n"

    t = int(input("Podaj t: "))
    assert t % 2 == 0 and t > 0, "Bledne t"

    streak = 0
    last_cena = None
    last_last_cena = None

    magazyn_n = 0
    obrot_s = obrot_n = 0
    

    for i in range(n):
        cena = int(input(f"Podaj cene w tygodniu {i+1}: "))
        assert cena > 0, "Bledna cena"

        if last_cena is not None and cena < last_cena:
            if streak >= 0:
                streak += 1
            else:
                streak = 1
        elif last_cena is not None and cena > last_cena:
            if streak <= 0:
                streak -= 1
            else:
                streak = -1
        else:
            streak = 0

        obrot_s += 0.15 * t * cena

        if streak >= 2:
            zakupiono = min(2 * t, 5 * t - magazyn_n)
        else:
            zakupiono = min(1 / 2 * t, 5 * t - magazyn_n)
        magazyn_n += zakupiono
        obrot_n -= zakupiono * cena

        if streak <= -2:
            p = (cena - last_last_cena) / last_last_cena * 5 * t
        else:
            p = 0
        
        if i + 1 == n:
            sprzedano = magazyn_n
        else:
            sprzedano = min(1 / 2 * t + p, magazyn_n)
        magazyn_n -= sprzedano
        obrot_n += 1.15 * cena * sprzedano

        last_last_cena = last_cena
        last_cena = cena

        print(f"Nowy model zakupil {zakupiono}, sprzedano {sprzedano}, zostalo w magazynie {magazyn_n}")
        print(f"Nowy model dochod {obrot_n}")
        print(f"Stary model dochod {obrot_s}")

    print()
    print(f"Nowy model dochod podsumowanie - {obrot_n}")
    print(f"Stary model dochod podsumowanie - {obrot_s}")
    if obrot_n > obrot_s:
        print(f"Nowy model mial wiekszy dochod o {obrot_n - obrot_s}")
    elif obrot_n < obrot_s:
        print(f"Stary model mial wiekszy dochod o {obrot_s - obrot_n}")
    else:
        print("Dochody obu byly identyczne")    

if __name__ == '__main__':
    main()