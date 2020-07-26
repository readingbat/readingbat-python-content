# @desc This is a description of for loop 3

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
    print(for_loop3('aaaaa', 5))


if __name__ == '__main__':
    main()
