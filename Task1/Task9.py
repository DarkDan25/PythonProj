import re


def main(x):
    matches = re.findall(r"\s*(-*[0-9]*)\sto\s*([^\n][a-z]*_*[0-9]*)", x)
    return [(value, int(key)) for key, value in matches]


if __name__ == '__main__':
    print(main(
        "<data><data>loc #8469 to usreri. </data><data>loc#7581 to inedre. </data> <data> loc#-6731 to tiis. </data> </data>"))
    print(main(
        "<data> <data>loc #3619 to ares_784. </data><data> loc#-9432 to\nraarle_593. </data><data> loc #7796 to soxege_65. </data> <data>\nloc#5901 to zasoan_202.</data></data>"))
