# @desc **.strip()** removes whitespace from both ends of a string but not the middle.

def strip1(s):
    return s.strip()


def main():
    print(strip1('  hello  '))
    print(strip1('world'))
    print(strip1('  hi there  '))
    print(strip1(''))
    print(strip1('   '))


if __name__ == '__main__':
    main()
