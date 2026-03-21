# @desc **.isdigit()** returns True only if every character in the string is a digit. An empty string returns False.

def isdigit1(s):
    return s.isdigit()


def main():
    print(isdigit1('123'))
    print(isdigit1('hello'))
    print(isdigit1('12a'))
    print(isdigit1(''))
    print(isdigit1('0'))
    print(isdigit1('99999'))


if __name__ == '__main__':
    main()
