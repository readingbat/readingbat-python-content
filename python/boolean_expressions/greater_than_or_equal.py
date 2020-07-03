def greater_than_or_equal(val1, val2):
    result = val1 >= val2
    return result


def main():
    print(greater_than_or_equal(6, 4))
    print(greater_than_or_equal(12, 12))
    print(greater_than_or_equal(8, 8))
    print(greater_than_or_equal(12, 24))
    print(greater_than_or_equal(7, 2))


if __name__ == '__main__':
    main()
