def combine2(s1, s2):
    s1 = s1.substring(1)
    s2 = s2.substring(1)
    result = s1 + s2
    return result


def main():
    print(combine2('Car', 'wash'))
    print(combine2(' Hello', '  world'))
    print(combine2('55', '88'))
    print(combine2('Snow', 'ball'))
    print(combine2('Rain', 'boots'))
    print(combine2('Reading', 'bat'))
    print(combine2('AA', 'HI'))
    print(combine2('Hi', 'there'))
    print(combine2(' ', ' '))

if __name__ == '__main__':
    main()