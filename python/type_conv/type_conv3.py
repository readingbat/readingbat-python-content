# @desc **float()** converts an integer to a decimal number, adding **.0** to the end.

def type_conv3(n):
    return str(float(n))


def main():
    print(type_conv3(5))
    print(type_conv3(0))
    print(type_conv3(-3))
    print(type_conv3(100))
    print(type_conv3(1))


if __name__ == '__main__':
    main()
