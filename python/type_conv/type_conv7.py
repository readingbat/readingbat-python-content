# @desc Multiplying a string by an integer repeats it that many times. Multiplying by 0 gives an empty string.

def type_conv7(s, n):
    return s * n


def main():
    print(type_conv7('ha', 3))
    print(type_conv7('x', 5))
    print(type_conv7('hi', 0))
    print(type_conv7('ab', 1))
    print(type_conv7('!', 4))


if __name__ == '__main__':
    main()
