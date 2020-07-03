def less_than(val1, val2):
    result = val1 < val2
    return result


def main():
    print(less_than(4, 6))
    print(less_than(8, 12))
    print(less_than(19, 19))
    print(less_than(12, 8))
    print(less_than(11, 28))


if __name__ == "__main__":
    main()
