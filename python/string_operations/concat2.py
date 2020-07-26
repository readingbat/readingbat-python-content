def concat2(s1, s2, s3):
    result = s1 + s2 + s3
    return result


def main():
    print(concat2('Car', 'wash', ' needed'))
    print(concat2('He', 'llo', ' world'))
    print(concat2('5', '8', '1'))
    print(concat2('Snow', 'ball', ' fight'))
    print(concat2('Rain', 'boots', ''))
    print(concat2('Reading', 'bat', ' is fun'))
    print(concat2('', 'Hi', ''))
    print(concat2('', '', ''))
    print(concat2(' ', ' ', ' '))


if __name__ == '__main__':
    main()
