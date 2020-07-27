def if_stmt2(x):
    if x > 10:
        x+=5
    else:
        return x
    return x

def main():
    print(if_stmt2(5))
    print(if_stmt2(15))
    print(if_stmt2(0))
    print(if_stmt2(10))
    print(if_stmt2(13))
    print(if_stmt2(20))
    print(if_stmt2(3))


if __name__ == '__main__':
    main()
