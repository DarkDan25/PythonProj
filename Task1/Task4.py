from math import atan


def main(n):
    while n >= 1:
        return main(n - 1) - 46 * (atan(main(n - 1)) ** 3)
    return -0.74


print(f"{main(5):.2e}")
