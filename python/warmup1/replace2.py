def replace2(x):
    str = ''
    if x[0] != 'a':
        str += 'hi' + x[1:len(x) - 1]
    else:
        str += x[:len(x) - 1]
    if x[len(x) - 1] != 'z':
        str += 'hi'
    else:
        str += x[len(x) - 1]
    return str


def main():
    print(replace2('a hello '))
    print(replace2('goodbyez'))
    print(replace2('aworldz'))
    print(replace2('oof'))
    print(replace2('az'))
    print(replace2('   '))


if __name__ == '__main__':
    main()
