# @desc This is a description of for loop 1

def for_loop1(x):
    result = 0
    for i in x:
        result += 2
    return result


def main():
    print(for_loop1('hello'))
    print(for_loop1('world'))
    print(for_loop1('apples'))
    print(for_loop1(''))
    print(for_loop1('a'))
    print(for_loop1('oof'))


if __name__ == '__main__':
    main()
