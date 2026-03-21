# @desc **int()** on a float removes the decimal part without rounding — it always truncates toward zero.

def type_conv4(x):
    return int(x)


def main():
    print(type_conv4(3.7))
    print(type_conv4(3.2))
    print(type_conv4(-2.8))
    print(type_conv4(0.9))
    print(type_conv4(5.0))
    print(type_conv4(-0.5))


if __name__ == '__main__':
    main()
