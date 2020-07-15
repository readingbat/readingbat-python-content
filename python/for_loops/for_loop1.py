def forloop1(x):
    result = 0
    for i in range(x):
        result += 2
    return result


def main():
    print(forloop1(5))
    print(forloop1(2))
    print(forloop1(1))
    print(forloop1(15))
    print(forloop1(150))
    print(forloop1(10))


if __name__ == '__main__':
    main()
