def x_and_y(x, y):
    z = 0
    for i in range(x):
        z += 1
    return y - z


def main():
    print(x_and_y(5, 7))
    print(x_and_y(2, 5))
    print(x_and_y(1, 8))
    print(x_and_y(15, 1))
    print(x_and_y(150, 0))
    print(x_and_y(10, 10))


if __name__ == '__main__':
    main()
