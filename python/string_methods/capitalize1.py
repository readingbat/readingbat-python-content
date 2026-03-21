# @desc **.capitalize()** uppercases only the first character and lowercases everything else.

def capitalize1(s):
    return s.capitalize()


def main():
    print(capitalize1('hello'))
    print(capitalize1('HELLO'))
    print(capitalize1('hello world'))
    print(capitalize1(''))
    print(capitalize1('a'))


if __name__ == '__main__':
    main()
