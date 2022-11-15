# cx = float(input("Podaj cx: "))
# cy = float(input("Podaj cy: "))
# x0 = float(input("Podaj x0: "))
# y0 = float(input("Podaj y0: "))
# width = float(input("Podaj szerokość: "))
# res = int(input("Podaj rozdzielczosc symulacji: "))
# i = int(input("Podaj maksymalna liczbe iteracji dla jednego punktu: "))

cx = -0.123
cy = 0.745
x0 = y0 = 0.
width = 2
res = 31
i = 25

if width <= 0 or res <= 0 or i < 0 or res % 2 == 0:
    raise ValueError("Bledne dane")

x, y = x0, y0
i_c = 0

print(f"Trajektoria punktu {(x0, y0)}")
for _ in range(i):
    x, y = x ** 2 - y ** 2 + cx, 2 * x * y + cy
    i_c += 1

    if x ** 2 + y ** 2 > 4:
        break
    print((x, y))

step = width / (res - 1)
offset = (res - 1) / 2
x_start = x0 - step * offset
x_iter, y_iter = x_start, y0 + step * offset

wizualizacja = ""

for pkt in range(res * res):
    if pkt != 0 and pkt % res == 0:
        y_iter -= step
        x_iter = x_start
    else:
        x_iter += step
    x, y = x_iter, y_iter

# for j in range(res):
#     for i in range(res):
        # x = x0 + i * width / (res - 1) - width / 2
        # y = y0 - j * width / (res - 1) + width / 2

    for _ in range(i):
        x, y = x ** 2 - y ** 2 + cx, 2 * x * y + cy
        i_c += 1
            
        if x ** 2 + y ** 2 > 4:
            break

    if x ** 2 + y ** 2 <= 4: # nie oddalil sie bardziej niz o 2
        wizualizacja += "@"
    else:
        wizualizacja += " "

l, r = 0, res
while l < len(wizualizacja):
    print(wizualizacja[l:r])
    l, r = r, r + res
print(f"Program wykonal w sumie {i_c} iteracji.")