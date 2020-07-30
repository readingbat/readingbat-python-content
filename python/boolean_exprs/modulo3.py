# @desc **% 2**" is an easy way of testing if a number is odd or even.

def modulo3(num):
    result = num % 2 == 1
    return result


def main():
    print(modulo3(9))
    print(modulo3(13))
    print(modulo3(10))
    print(modulo3(31))
    print(modulo3(8))


if __name__ == '__main__':
    main()
