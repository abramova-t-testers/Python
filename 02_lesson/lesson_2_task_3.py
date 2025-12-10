import math


def square(side):
    area = side ** 2
    if not isinstance(side, int):
        return math.ceil(area)
    else:
        return int(area)


n = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(n)}")
