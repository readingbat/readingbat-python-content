def combine2(s1, s2):
    s3 = s1[1]
    s4 = s2[1]
    result = s3 + s4
    return result


def main():
    print(combine2('Car', 'wash'))
    print(combine2(' Hello', ' world'))
    print(combine2('55', '88'))
    print(combine2('Snow', 'ball'))
    print(combine2('Rain', 'boots'))
    print(combine2('Reading', 'bat'))
    print(combine2('AA', 'HI'))
    print(combine2('Hi', 'there'))
    print(combine2('  ', '  '))


if __name__ == '__main__':
    main()
