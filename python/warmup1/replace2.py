def replace1(x):
    str = ''
    if x[0] != 'a':
        str += 'hi' + x[1:len(x)-1]
    else:
        str += x[:len(x)-1]
    if x[len(x)-1] != 'z':
        str += 'hi'
    else:
        str += x[len(x)-1]
    return str


def main():
    print(replace1('a hello '))
    print(replace1('goodbyez'))
    print(replace1('aworldz'))
    print(replace1('oof'))
    print(replace1('az'))
    print(replace1('   '))

if __name__ == '__main__':
    main()