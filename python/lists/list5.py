def list5(x, y, z):
    result = []
    for i in range(x, y, z):
        result.append(i)
    return result


def main():
    print(list5(0, 5, 2))
    print(list5(10, 5, -1))
    print(list5(20, 0, -4))
    print(list5(10, 5, 2))

if __name__ == '__main__':
    main()