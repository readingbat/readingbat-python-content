def for_loop1(x):
    result = 0
    for i in range(x):
        result += 2
    return result


def main():
    print(for_loop1(5))
    print(for_loop1(2))
    print(for_loop1(1))
    print(for_loop1(15))
    print(for_loop1(150))
    print(for_loop1(10))


if __name__ == '__main__':
    main()
