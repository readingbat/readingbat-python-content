# @desc Determine if one value is greater than another with the **>** operator.

def greater_than(val1, val2):
    result = val1 > val2
    return result


def main():
    print(greater_than(4, 6))
    print(greater_than(8, 12))
    print(greater_than(19, 19))
    print(greater_than(12, 8))
    print(greater_than(11, 28))


if __name__ == '__main__':
    main()
