import math


def f(a, b):
    return a / b


def main(x, z):
    a = 40 * pow(x, 2) - f(pow(x, 2) - pow(z, 3) - x, 83)
    b = pow(z, 5) + pow(85 * pow(x, 3) + 77, 6)
    c = f(pow(z, 18), 42) - pow(math.log2(x), 5)
    d = pow(83 * pow(x, 3) - z - 74, 6) - 86 * z
    return f(a, b) + f(c, d)


f"{main(0.71, 0.53):.2e}"
