# @desc **.title()** capitalizes the first letter of each word and lowercases the rest.

def title1(s):
    return s.title()


def main():
    print(title1('hello world'))
    print(title1('HELLO'))
    print(title1('hello'))
    print(title1('a b c'))
    print(title1(''))


if __name__ == '__main__':
    main()
