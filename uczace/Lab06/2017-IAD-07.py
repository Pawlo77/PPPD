import math
import random

def distance(x, y):
    distance = 0
    for xi, yi in zip(x, y):
        distance += (xi - yi) ** 2
    return math.sqrt(distance)

def random_point(n, a=-1, b=1):
    return [random.uniform(a, b) for _ in range(n)]

def volume_exact(n):
    return math.pi ** (n / 2) / (math.gamma() * (n / 2 + 1))

def unit_ball_ratio(n):
    ball_v = volume_exact(n)
    # return 

def volume_approx(n, m=10000):
    