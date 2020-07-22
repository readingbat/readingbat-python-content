def for_loop2(x, y):
    z = 0
    for i in range(x):
        z += 1
    return y - z


def main():
    print(for_loop2(5, 7))
    print(for_loop2(2, 5))
    print(for_loop2(1, 8))
    print(for_loop2(15, 1))
    print(for_loop2(150, 0))
    print(for_loop2(10, 10))


if __name__ == '__main__':
    main()
