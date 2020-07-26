def for_loop2(x):
    result = 0
    for i in x:
        if i == 'a':
            result += 1
    return result


def main():
    print(for_loop2('athenian'))
    print(for_loop2('apples'))
    print(for_loop2('hello'))
    print(for_loop2(''))
    print(for_loop2(' '))
    print(for_loop2('alphabet'))


if __name__ == '__main__':
    main()
