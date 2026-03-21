# @desc Convert a string to an integer first with **int()**, then you can perform arithmetic on it.

def type_conv9(s):
    return int(s) * 2


def main():
    print(type_conv9('5'))
    print(type_conv9('0'))
    print(type_conv9('100'))
    print(type_conv9('-3'))
    print(type_conv9('7'))


if __name__ == '__main__':
    main()
