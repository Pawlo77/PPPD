def main():
    n = int(input("Podaj n: "))
    assert n > 5, "Błędne n"

    k = int(input("Podaj k: "))
    assert k > 0, "Błędne k"

    g1 = g2 = k
    g1_budget = g2_budget = 0
    cur_c = last_c = None
    streak_g1 = 0

    for i in range(n):
        cur_c = float(input(f"Podaj cene wegla w tygodniu {i + 1}: "))
        assert cur_c > 0, "Cena węgla musi być dodatnia"

        if i + 1 == n:
            if g1 > 0:
                g1_budget += g1 * cur_c
                print(f"Pierwszy gospodarz kupil {g1} worków wegla")
            if g2 > 0:
                g2_budget += g2 * cur_c
                print(f"Pierwszy gospodarz kupil {g2} worków wegla")
            break

        if last_c is not None and cur_c < last_c:
            streak_g1 += 1
            if g2 >= 2:
                g2 -= 2
                g2_budget += 2 * cur_c
                print("Drugi gospodarz kupil 2 worki wegla")
            elif g2 == 1:
                g2 = 0
                g2_budget += cur_c
                print("Drugi gospodarz kupil 1 worek wegla")
        else:
            streak_g1 = 0

        if streak_g1 >= 3 and g1 > 0:
            g1 -= k / 4
            g1_budget += k / 4 * cur_c
            print(f"Pierwszy gospodarz kupil {k / 4} worków wegla")

        last_c = cur_c
        if g1 == 0 and g2 == 0:
            break

    print(f"Pierwszy gospodarz zaplacil {g1_budget} zł")
    print(f"Drugi gospodarz zaplacil {g2_budget} zł")

    if g1_budget < g2_budget:
        print(f"Pierwszy gospodarz zaplacil o {g2_budget - g1_budget} zł mniej")
    elif g1_budget > g2_budget:
        print(f"Drugi gospodarz zaplacil o {g1_budget - g2_budget} zł mniej")
    else:
        print(f"Obaj gospodarze zaplacili tyle samo")

if __name__ == "__main__":
    main()
