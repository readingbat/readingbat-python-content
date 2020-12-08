def replace3(x):
    if len(x) <= 4:
        return x
    str = x[len(x) - 2:] + x[2: len(x) - 2] + x[0:2]
    return str


def main():
    print(replace3('hello'))
    print(replace3('goodbye'))
    print(replace3(' world '))
    print(replace3(''))
    print(replace3('oof'))
    print(replace3('a'))


if __name__ == '__main__':
    main()
