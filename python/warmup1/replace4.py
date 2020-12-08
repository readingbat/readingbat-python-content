def replace4(x):
    if len(x) <= 1:
        return x
    if x[0] == x[len(x) - 1]:
        return x[0] + x
    return x + x[len(x) - 1]


def main():
    print(replace4('hello'))
    print(replace4('aba'))
    print(replace4(' world'))
    print(replace4(''))
    print(replace4('goodbye'))
    print(replace4('oof'))
    print(replace4('a'))


if __name__ == '__main__':
    main()
