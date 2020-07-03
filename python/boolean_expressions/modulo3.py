def is_odd(num):
    result = num % 2 == 1
    return result


def main():
    print(is_odd(9))
    print(is_odd(13))
    print(is_odd(10))
    print(is_odd(31))
    print(is_odd(8))


if __name__ == '__main__':
    main()
