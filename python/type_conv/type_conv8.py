# @desc Converting a number to a string with **str()** lets you count its digits using **len()**.

def type_conv8(x):
    return len(str(x))


def main():
    print(type_conv8(123))
    print(type_conv8(0))
    print(type_conv8(-5))
    print(type_conv8(9999))
    print(type_conv8(10))
    print(type_conv8(1000000))


if __name__ == '__main__':
    main()
