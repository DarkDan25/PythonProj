def main(num):
    code = [4, 2, 7, 8, 2]
    move1 = [0, 4, 6, 13, 21]
    move2 = [19, 9, 0, 11, 7]
    result = 0
    for i in range(len(code)):
        h = (((int(num)) >> move1[i]) & int('1' * code[i], 2)) << move2[i]
        result |= h
    return str(result)


if __name__ == '__main__':
    print(main('817860'))
# print(encode_data(decode_data(817860)))
