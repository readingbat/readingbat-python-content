# @desc **str[y:]** returns a substring starting at index y

def for_loop5(str, x, y):
    result = 0
    for i in str[y:]:
        if i == x:
            result += 1
    return result


def main():
    print(for_loop5('athenian', 'e', 2))
    print(for_loop5('apples', 'p', 1))
    print(for_loop5('hello', 'a', 3))
    print(for_loop5('aa', 'a', 1))


if __name__ == '__main__':
    main()
