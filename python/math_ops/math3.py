# @desc The __**__ operator raises a number to a power. **x \*\* y** means x multiplied by itself y times.

def math3(x, y):
    return x ** y


def main():
    print(math3(2, 3))
    print(math3(3, 2))
    print(math3(5, 0))
    print(math3(10, 1))
    print(math3(2, 10))
    print(math3(1, 100))


if __name__ == '__main__':
    main()
