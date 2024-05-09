from math import cos
from math import ceil


def main(y):
    if y < 35:
        return y + 93 * pow(y, 2) + 20 * pow(y, 3) + 22
    elif 35 <= y < 117:
        return 91 * (pow(y, 2) - y - 1) - 1 - 2 * pow(cos(y), 3)
    elif 117 <= y < 181:
        a = 66 * pow(cos(y), 4)
        b = 63 * pow(67 * pow(y, 2) - (y / 11), 5)
        c = 77 * pow(ceil(y) - 1, 3)
        return a - b - c
    else:
        a = pow(abs(99 * pow(y, 3) - 2 * pow(y, 2)), 3)
        return a + 8 + 48 * y - pow(y, 2)


f"{main(109):.2e}"
