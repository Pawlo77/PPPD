WIDTH = 10
HEIGHT = int(input("height: "))

# if HEIGHT not in [7, 9, 11]: 
    # raise ValueError("HEIGHT not in [7, 9, 11]")

x = int(input("x: "))
o = int(input("o: "))
tx = float(input("czas przyklejania jednostki x: "))
to = tx / 3
tz = 3 * tx

if not (x > 0 and o > 0 and x <= WIDTH - 1 and o <= x / 2):
    raise ValueError("Dane o rolkach nie spelniaja zalozen zadania.")

sciana = [
    ["0" for _ in range(WIDTH)] for _ in range(HEIGHT)
]

for i in range(3):
    for j in range(3):
        sciana[HEIGHT - 3 - i][WIDTH - 3 - j] = " "

cur_o = o
cur_x = x
num_o = 1 
num_x = 1
all_t = 2 * tz

for i in range(HEIGHT):
    for j in range(WIDTH):
        if sciana[i][j] == " ":
            continue

        if cur_o != 0:
            cur_o -= 1
            sciana[i][j] = "o"
            all_t += to
        elif cur_x != 0:
            cur_x -= 1
            sciana[i][j] = "x"
            all_t += tx
        else:
            cur_o = o - 1
            cur_x = x

            num_o += 1
            num_x += 1
            sciana[i][j] = "o"
            all_t += to + 2 * tz

if cur_x == x:
    num_x -= 1
    all_t -= tz

for row in sciana:
    print("".join(row))

print("Calkowity czas malowania to", all_t)
print(f"Zuzyto {num_x} rolek x i {num_o} rolek o")
