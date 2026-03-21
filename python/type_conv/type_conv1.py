# @desc **int()** converts a string of digits into an integer so you can do math with it.

def type_conv1(s):
    return int(s)


def main():
    print(type_conv1('42'))
    print(type_conv1('0'))
    print(type_conv1('100'))
    print(type_conv1('-5'))
    print(type_conv1('7'))


if __name__ == '__main__':
    main()
