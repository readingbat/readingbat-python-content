# @desc Determine if two value are equal with the **==** operator. Notice the 2 **=** characters.

def equal(val1, val2):
    result = val1 == val2
    return result


def main():
    print(equal(6, 6))
    print(equal(12, 12))
    print(equal(8, 7))
    print(equal(12, 24))
    print(equal(7, 7))


if __name__ == '__main__':
    main()
