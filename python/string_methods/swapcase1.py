# @desc **.swapcase()** flips uppercase letters to lowercase and lowercase to uppercase.

def swapcase1(s):
    return s.swapcase()


def main():
    print(swapcase1('Hello'))
    print(swapcase1('HELLO'))
    print(swapcase1('hello'))
    print(swapcase1('HeLLo WoRLd'))
    print(swapcase1(''))


if __name__ == '__main__':
    main()
