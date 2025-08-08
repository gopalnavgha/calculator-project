import math
from typing import Tuple

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError('Division by zero')
    return a / b

def power(a, b):
    return a ** b

def square(a):
    return a * a

def sqrt(a):
    if a < 0:
        raise ValueError('Square root of negative number')
    return math.sqrt(a)

def area_rectangle(length, width):
    return length * width

def area_circle(radius):
    return math.pi * radius * radius

def area_triangle(base, height):
    return 0.5 * base * height

def quadratic_roots(a, b, c) -> Tuple[complex, complex]:
    disc = b * b - 4 * a * c
    if disc >= 0:
        sqrt_disc = math.sqrt(disc)
    else:
        sqrt_disc = complex(0, math.sqrt(-disc))
    r1 = (-b + sqrt_disc) / (2 * a)
    r2 = (-b - sqrt_disc) / (2 * a)
    return r1, r2

def simple_interest(p, r, t):
    return (p * r * t) / 100.0

def compound_interest(p, r, t, n=1):
    return p * ((1 + r / (100.0 * n)) ** (n * t))

def bmi(weight_kg, height_m):
    if height_m <= 0:
        raise ValueError('Height must be > 0')
    return weight_kg / (height_m ** 2)

def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)
