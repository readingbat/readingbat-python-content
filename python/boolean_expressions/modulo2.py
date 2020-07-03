def is_even(num):
    result = num % 2
    return result == 0


def main():
    print(is_even(9))
    print(is_even(13))
    print(is_even(10))
    print(is_even(31))
    print(is_even(8))


if __name__ == '__main__':
    main()
