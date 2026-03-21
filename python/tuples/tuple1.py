# @desc Tuples use the same indexing as lists — the first element is at index **0**.

def tuple1(t):
    return str(t[0])


def main():
    print(tuple1((1, 2, 3)))
    print(tuple1(('a', 'b')))
    print(tuple1((10,)))
    print(tuple1((True, False)))


if __name__ == '__main__':
    main()
