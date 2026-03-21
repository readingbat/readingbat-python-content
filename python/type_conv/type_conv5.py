# @desc **bool()** converts values to True or False. Zero, empty strings, and empty lists are False; most other values are True.

def type_conv5(x):
    return bool(x)


def main():
    print(type_conv5(0))
    print(type_conv5(1))
    print(type_conv5(-1))
    print(type_conv5(''))
    print(type_conv5('hello'))
    print(type_conv5([]))
    print(type_conv5([1]))


if __name__ == '__main__':
    main()
