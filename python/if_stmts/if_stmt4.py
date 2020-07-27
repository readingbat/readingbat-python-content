def if_stmt4(x, y, z):
    if x and y > z:
        return y
    else:
        return z


def main():
    print(if_stmt4(True, 3, 1))
    print(if_stmt4(False, 3, 1))
    print(if_stmt4(True, 10, 3))
    print(if_stmt4(False, 11, 3))
    print(if_stmt4(False, 51, 32))
    print(if_stmt4(True, 1, 0))


if __name__ == '__main__':
    main()
