def if_stmt1(x):
    if x > 10:
        return x
    return 3


def main():
    print(if_stmt1(5))
    print(if_stmt1(15))
    print(if_stmt1(0))
    print(if_stmt1(10))
    print(if_stmt1(13))
    print(if_stmt1(20))
    print(if_stmt1(3))


if __name__ == '__main__':
    main()
