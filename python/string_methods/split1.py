# @desc **.split()** with no arguments breaks a string at whitespace and returns a list.

def split1(s):
    return s.split()


def main():
    print(split1('hello world'))
    print(split1('a b c'))
    print(split1('hello'))
    print(split1('  hello  '))
    print(split1('a  b'))


if __name__ == '__main__':
    main()
