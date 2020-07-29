# @desc **% 2**" is an easy way of testing if a number is odd or even.

def modulo2(num):
    result = num % 2
    return result == 0


def main():
    print(modulo2(9))
    print(modulo2(13))
    print(modulo2(10))
    print(modulo2(31))
    print(modulo2(8))


if __name__ == '__main__':
    main()
