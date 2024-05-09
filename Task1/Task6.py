from math import floor


def main(e):
    B = {la for la in e if -28 < la <= 32}
    E = {abs(b) - (6 * b) for b in B if b > -4}
    delt = {3 * la + abs(b) for la in e for b in B if la < b}
    H = {abs(q) + q % 3 for q in delt if q <= 30}

    return sum(v % 2 for v in E) + sum(floor(v / 6)
                                       + 9 * n for v in E for n in H)


main({-63, 1, 99, 37, 38, -55, -22, -50, -42, -41})
