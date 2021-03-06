# @desc **str[x:]** returns a substring starting at index x

def for_loop3(str, x):
    result = 0
    for i in str[x:]:
        if i == 'a':
            result += 1
    return result


def main():
    print(for_loop3('athenian', 1))
    print(for_loop3('apples', 2))
    print(for_loop3('hello', 3))
    print(for_loop3('alphabet', 0))
    print(for_loop3('aaaaa', 3))
    print(for_loop3('aaaaa', 4))
    print(for_loop3('aaaaa', 5))


if __name__ == '__main__':
    main()
