def if_stmt3(x, y):
    if x > 10 and y == True:
        x+=5
    else:
        return x
    return x

def main():
    print(if_stmt3(15, True))
    print(if_stmt3(15, False))
    print(if_stmt3(0, True))
    print(if_stmt3(10, True))
    print(if_stmt3(13, False))
    print(if_stmt3(20, True))
    print(if_stmt3(3, False))


if __name__ == '__main__':
    main()
