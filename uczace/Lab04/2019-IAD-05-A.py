import random

def drzewo(x, y):
    if x >= 0 and x <= 10 and y >= 0 and y <= 10:
        return (x == y) and (x % 10 < 4 or x % 10 > 5)
    elif x >= -10 and x <= -1 and y >= 0 and y <= 10:
        return True
    else:
        return False

def wypisz_prostokat(x_min, x_max, y_min, y_max):
    print(f"[{x_min}, {x_max}] x [{y_min}, {y_max}]")

def najmniejszy_plot(x_min, x_max, y_min, y_max):
    dx_min = x_max
    dx_max = x_min
    dy_min = y_max
    dy_max = y_min
    d = False

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            if drzewo(x, y):
                d = True

                if x < dx_min:
                    dx_min = x
                if x > dx_max:
                    dx_max = x
                if y < dy_min:
                    dy_min = y
                if y > dy_max:
                    dy_max = y

    if not d:
        return (0, 0, 0, 0)
    return (dx_min, dx_max, dy_min, dy_max)

def zapisz_do_pliku(sciezka, x_min, x_max, y_min, y_max):
    l0 = max(len(str(y_max)), 5)
    l1 = len(str(x_max))

    with open(sciezka, 'w') as f:
        for y in range(y_min, y_max + 1):
            row = f"{str(y):{l0}.{l0}s}"

            for x in range(x_min, x_max + 1):
                if drzewo(x, y):    
                    row += f"{'D':{l1}.{l1}s}"
                else:
                    row += f"{'.':{l1}.{l1}s}"
            
            f.write(row + "\n")

        row = f"{'y, x':{l0}.{l0}s}"
        for x in range(x_min, x_max + 1):
            row += f"{str(x):{l1}.{l1}s}"
        f.write(row + "\n")

def obwod_prostokata(x_min, x_max, y_min, y_max):
    return 2 * (x_max - x_min) + 2 * (y_max - y_min)

def najlepszy_podzial(x_min, x_max, y_min, y_max):
    sm = float("inf")
    x_b = None

    for x in range(x_min + 1, x_max):
        p1 = obwod_prostokata(*najmniejszy_plot(x_min, x, y_min, y_max))
        p2 = obwod_prostokata(*najmniejszy_plot(x + 1, x_max, y_min, y_max))

        if p1 + p2 < sm:
            sm = p1 + p2
            x_b = x

    return x_b

def drzewo2(x, y):
    if x < -10 or x > 10 or y < -10 or y > 10:
        return False
    if 0 <= x <= 10 and -10 <= y <= 10:
        return True if random.choice([1, 2]) == 1 else False
    return True if random.choice(list(range(10))) == 0 else False

def main():
    x_min = int(input("Min x: "))
    x_max = int(input("Max x: "))
    y_min = int(input("Min y: "))
    y_max = int(input("Max y: "))

    d = (x_min, x_max, y_min, y_max)
    
    wypisz_prostokat(*d)
    plot = najmniejszy_plot(*d)
    wypisz_prostokat(*plot)
    zapisz_do_pliku("ogrod.txt", *d)
    
    print(f"Obwód sadu: {obwod_prostokata(*d)}")
    print(f"Dlugosc plotu: {obwod_prostokata(*plot)}")
    print(f"Najlepszy podzial to {najlepszy_podzial(*d)}")


if __name__ == "__main__":
    main()