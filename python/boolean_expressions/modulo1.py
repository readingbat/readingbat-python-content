# @desc The "**%**" operator returns the remainder after dividing two numbers. See more details [here](https://blog.mattclemente.com/2019/07/12/modulus-operator-modulo-operation.html).
# """.trimIndent()

def modulo1(num, mod):
    result = num % mod
    return result


def main():
    print(modulo1(9, 2))
    print(modulo1(13, 2))
    print(modulo1(10, 5))
    print(modulo1(30, 4))
    print(modulo1(8, 1))


if __name__ == '__main__':
    main()
