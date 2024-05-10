def x3(x, right):
    if x[3] == 1994:
        return right
    elif x[3] == 1973:
        return 11


def x2(x, mid, right):
    if x[2] == "NL":
        return 10
    elif x[2] == "RED":
        return mid
    elif x[2] == "M":
        return right


def x1(x, left, mid, right):
    if x[1] == 2015:
        return left
    elif x[1] == 1969:
        return mid
    elif x[1] == 2013:
        return right


def x4(x):
    if x[4] == 1997:
        return 4
    elif x[4] == 2009:
        return 3
    elif x[4] == 2006:
        return 2


def x0(x):
    if x[0] == 1986:
        return 7
    elif x[0] == 2012:
        return 6
    elif x[0] == 1992:
        return 5


def main(x):
    return x3(x, x2(x, x1(x, 9, 8, x0(x)), x1(x, x4(x), 1, 0)))


# print(main([1986, 1969, 'RED', 1973, 1997]))
assert main([1986, 1969, 'RED', 1973, 1997]) == 11
assert main([2012, 2015, 'M', 1994, 1997]) == 4
assert main([2012, 2013, 'NL', 1994, 2006]) == 10
assert main([2012, 2015, 'M', 1994, 2006]) == 2
assert main([1992, 1969, 'RED', 1994, 1997]) == 8
