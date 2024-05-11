from struct import unpack_from, calcsize


class Types:
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'
    float = 'f'
    double = 'd'


class BinaryReader:
    def __init__(self, data, offset, order=">"):
        self.data = data
        self.offset = offset
        self.order = order

    def jump(self, offset):
        return BinaryReader(self.data, offset, self.order)

    def read(self, pattern):
        data = unpack_from(self.order + pattern, self.data, self.offset)
        self.offset += calcsize(pattern)
        return data[0]


def read_d(reader: BinaryReader):
    d1 = reader.read(Types.int64)
    d2 = [reader.read(Types.uint32) for _ in range(6)]
    return dict(D1=d1, D2=d2)


def read_c(reader: BinaryReader):
    c1 = reader.read(Types.uint64)
    c2 = reader.read(Types.float)
    c3 = reader.read(Types.int16)
    return dict(C1=c1, C2=c2, C3=c3)


def read_b(reader: BinaryReader):
    b1size = reader.read(Types.uint32)
    b1address = reader.read(Types.uint32)
    b1 = []
    b1reader = reader.jump(b1address)
    for _ in range(b1size):
        address = b1reader.read(Types.uint16)
        tmpreader = b1reader.jump(address)
        b1.append(read_c(tmpreader))
    b2 = reader.read(Types.int8)
    b3 = read_d(reader)
    b4 = reader.read(Types.uint32)
    b5 = [reader.read(Types.uint32) for _ in range(5)]
    b6 = reader.read(Types.int32)
    b7 = reader.read(Types.uint8)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7)


def read_a(reader: BinaryReader):
    a1size = reader.read(Types.uint32)
    a1address = reader.read(Types.uint16)
    a1reader = reader.jump(a1address)
    a1 = ""
    for _ in range(a1size):
        a1 += a1reader.read(Types.char).decode()
    a2 = reader.read(Types.uint8)
    a3address = reader.read(Types.uint16)
    a3reader = reader.jump(a3address)
    a3 = read_b(a3reader)
    a4 = reader.read(Types.uint64)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4)


def main(bytes):
    reader = BinaryReader(bytes, 3)
    return read_a(reader)


a = (b'TNB\x00\x00\x00\x03\x00\x14e\x007U>\xaaF\x94\x11\xe1&erq\xf1M\x8e\x88\xc1'
     b'#\xcdW\xbfT\xc1[DL\x88\xb67\xdc\xce\x8bQ =\x19\x05\xa0_\x1a\x00\x17\x00%\x00'
     b'\x00\x00\x02\x00\x00\x003v~7\xbbk<\xe4%\xad\xce1}\xd4\xcc!\x94\xde;(=}'
     b'\xcf\x15~Ez`\xa1\x85\xd6\x894J\x83Q\x0eu\x18\x9c\x9e>q\xb1\x85\xaf'
     b'k\x17\xe8\xa8\x03\xf2P\xfb.\x13\xf1n\x9b\xc6\x00\xe6\x97')

print(main(a))
