def strlen3(s, t):
    length = len(2 * s) + len(3 * t)
    return length


def main():
    print(strlen3('ant', 'duck'))
    print(strlen3('', ''))
    print(strlen3('', '78'))
    print(strlen3('rock', 'sand'))
    print(strlen3('ex', 'ball'))


if __name__ == '__main__':
    main()
