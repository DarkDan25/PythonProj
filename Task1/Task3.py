def main(a, n, m, p):
    f = 0
    for c in range(1, m + 1):
        for k in range(1, n + 1):
            for j in range(1, a + 1):
                a1 = pow(j, 6)
                b = (92 * pow(74 * pow(p, 2) - 93 * k, 2))
                f += (a1 + b + pow(c, 2) - 94 * c - 38)
    return f


f"{main(2, 2, 4, 0.29):.2e}"
