def replace1(x):
    str = 'hi' + x[1:len(x) - 1] + 'hi'
    return str


def main():
    print(replace1('hello'))
    print(replace1('goodbye'))
    print(replace1(' world '))
    print(replace1(''))
    print(replace1('   '))
    print(replace1('oof'))


if __name__ == '__main__':
    main()
