# @desc **str()** converts a number into a string so you can concatenate it with other strings.

def type_conv2(n):
    return str(n)


def main():
    print(type_conv2(42))
    print(type_conv2(0))
    print(type_conv2(-5))
    print(type_conv2(100))
    print(type_conv2(7))


if __name__ == '__main__':
    main()
