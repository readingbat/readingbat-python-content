def if_statements2(x):
    if x > 10:
        x+=5
    else:
        return x
    return x

def main():
    print(if_statements2(5))
    print(if_statements2(15))
    print(if_statements2(0))
    print(if_statements2(10))
    print(if_statements2(13))
    print(if_statements2(20))
    print(if_statements2(3))


if __name__ == '__main__':
    main()
