# @desc Each string must be converted to an integer with **int()** before adding them together.

def type_conv10(strs):
    result = 0
    for s in strs:
        result += int(s)
    return result


def main():
    print(type_conv10(['1', '2', '3']))
    print(type_conv10(['10']))
    print(type_conv10(['0', '0']))
    print(type_conv10(['-1', '1']))
    print(type_conv10(['5', '5', '5']))


if __name__ == '__main__':
    main()
