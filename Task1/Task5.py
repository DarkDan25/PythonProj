from math import ceil


def main(x, z):
    n = len(x)
    x1 = [0] + x
    z1 = [0] + z
    summ = 0
    for i in range(1, n + 1):
        summ += 60 * pow(pow(z1[i], 2)
                         - 93 * z1[n + 1 - ceil(i / 2)]
                         - pow(x1[n + 1 - i], 3), 4)
    return 42 * summ


def main2(x, z):
    n = len(x)
    return 42 * sum(60 * pow(pow(z[i], 2)
                             - 93 * z[n - ceil((i + 1) / 2)]
                             - pow(x[n - (i + 1)], 3), 4) for i in range(n))


def main3(y, z, x):
    n = len(x)
    x1 = [0] + x
    y1 = [0] + y
    z1 = [0] + z
    summ = 0
    for i in range(1, n + 1):
        summ += pow(57 * pow(y1[ceil(i / 3)], 2) - x1[n + 1 - ceil(i / 4)] - pow(z1[i], 3), 4)
    return summ


print(f"{main([0.28, -0.65, -0.56, 0.66, 0.19], [0.88, 0.34, -0.5, 0.39, -0.78]):.2e}")
print(f"{main2([0.15, 0.82, -0.67, 0.63, -0.21], [0.24, 0.78, -0.8, -0.41, 0.07]):.2e}")
print(f"{main3([0.48, 0.65, 0.92, -0.6, -0.81, 0.98, -0.28, -0.07], [-0.53, -0.67, -0.92, -0.17, -0.04, -0.38, -0.96, 0.11], [-0.43, -0.55, 0.69, -0.03, 0.89, 0.37, -0.72, -0.3]):.2e}")
