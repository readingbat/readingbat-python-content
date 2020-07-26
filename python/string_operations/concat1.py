# @desc Merge two strings.

def concat1(s1, s2):
    result = s1 + s2
    return result


def main():
    print(concat1('Car', 'wash'))
    print(concat1('Hello', ' world'))
    print(concat1('5', '8'))
    print(concat1('Snow', 'ball'))
    print(concat1('Rain', 'boots'))
    print(concat1('Reading', 'bat'))
    print(concat1('', 'Hi'))
    print(concat1('', ''))
    print(concat1(' ', ' '))


if __name__ == '__main__':
    main()
