# @desc Determine if two value are not equal with the "**!=**" operator.

def not_equal(val1, val2):
    result = val1 != val2
    return result


def main():
    print(not_equal(9, 9))
    print(not_equal(22, 22))
    print(not_equal(8, 7))
    print(not_equal(12, 24))
    print(not_equal(6, 4))


if __name__ == '__main__':
    main()
