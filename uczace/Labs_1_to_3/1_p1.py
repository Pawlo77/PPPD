import math


DAYS = [
    31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]
WDAYS = [
    "niedziela", "poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota"
]


def get_data(mess, conn):
    try:
        x = int(input(mess))

        if conn(x):
            raise ValueError
    except Exception as e:
        print("\nBłędny format danych\n")
        return get_data(mess, conn)
    else:
        return x

def get_day(mess, month, year):
    try:
        x = int(input(mess))

        if check_day(x, month, year):
            raise ValueError
    except Exception as e:
        print("\nBłędny format danych\n")
        return get_day(mess, month, year)
    else:
        return x

def get_0():
    y0 = get_data("Podaj rok urodzenia: ", lambda y: not 1900 <= y <= 2022)
    m0 = get_data("Podaj miesiąc urodzenia: ", lambda m: not 1 <= m <= 12)
    d0 = get_day("Podaj dzień urodzenia: ", m0, y0)
    return d0, m0, y0

def get_1(d0, m0, y0):
    y = get_data("Podaj rok: ", lambda y: not 1900 <= y <= 2022)
    m = get_data("Podaj miesiąc: ", lambda m: not 1 <= m <= 12)
    d = get_day("Podaj dzień: ", m, y)

    if y < y0 or (y == y0 and m < m0) or (y == y0 and m == m0 and d < d0):
        print("\nData referencyjna nie moze byc wczesniejsza niz data urodzin.\n")
        return get_1(d0, m0, y0)
    return d, m, y

def check_day(d, m, y):
    if m == 2:
        if przestepny(y):
            return not 1 <= d <= 29
        return not 0 <= d <= 28
    return not 1 <= d <= DAYS[m - 1]

def przestepny(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

def check_period(d0, m0, d1, m1, day, month):
    if month == m0:
        return day >= d0
    if month == m1:
        return day <= d1
    return m0 < month < m1

def get_wday(d, m, y):
    Y = y - 1 if m < 3 else y
    y = Y % 100
    c = Y // 100
    m = (m - 2) % 12
    if m == 0: m = 12

    return (d + math.floor(2.6 * m - 0.2) + y + math.floor(y / 4) + math.floor(c / 4) - 2 * c) % 7

def get_days_1(d, m, y):
    if m == 2 and przestepny(y):
        return 29 - d
    return DAYS[m - 1] - d

d0, m0, y0 = get_0()

mess = "Urodziłeś się w"
if check_period(21, 3, 21, 6, d0, m0):
    print(mess, "wiosnę.")
elif check_period(22, 6, 22, 9, d0, m0): 
    print(mess, "lato.")
elif check_period(23, 9, 21, 12, d0, m0):
    print(mess, "jesień.")
else:
    print(mess, "zimę.")

print("Był to", WDAYS[get_wday(d0, m0, y0)], "\n")

d, m, y = get_1(d0, m0, y0)

y1 = y - y0
if m > m0:
    m1 = m - m0
    if d < d0:
        m1 -= 1
    d1 = d + get_days_1(d0, m0, y0) + 1

elif m == m0:
    if d >= d0:
        m1 = 0
        d1 = d - d0 + 1
    else:
        y1 = max(y1 - 1, 0)
        m1 = 11
        d1 = d + get_days_1(d0, m0, y0) + 1

else:
    y1 = max(y1 - 1, 0)
    m1 = 12 - m0 + m
    if d < d0:
        m1 -= 1
    d1 = d + get_days_1(d0, m0, y0) + 1

print(f"Masz {y1} lat, {m1} miesięcy, {d1} dni.")