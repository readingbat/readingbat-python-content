def for_loop3(str, x, y):
    result = 0
    for i in str[y:]:
        if i == x:
            result += 1
    return result


def main():
    print(for_loop3('athenian', 'e', 2))
    print(for_loop3('apples', 'ap', 1))
    print(for_loop3('hello', 'a', 3))
    print(for_loop3('alphabet', 'al', 0))
    print(for_loop3('aa', 'a', 1))

if __name__ == '__main__':
    main()