def combine1(s1, s2):
    s1 = s1.substring(0) + s1.substring(s1.length()-1)
    s2 = s2.substring(0) + s2.substring(s2.length()-1)
    result = s1 + s2
    return result


def main():
    print(combine1('Car', 'wash'))
    print(combine1('Hello', ' world'))
    print(combine1('5', '8'))
    print(combine1('Snow', 'ball'))
    print(combine1('Rain', 'boots'))
    print(combine1('Reading', 'bat'))
    print(combine1('AAA', 'Hi'))
    print(combine1('Hi', 'there'))
    print(combine1(' ', ' '))

if __name__ == '__main__':
    main()
