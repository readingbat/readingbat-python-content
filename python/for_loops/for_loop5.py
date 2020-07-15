def for_loop5(x, y, z):
    result = []
    for i in range(x, y, z):
        result.append(i)
    return result


def main():
    print(for_loop5(0, 5, 2))
    print(for_loop5(10, 5, -1))
    print(for_loop5(20, 0, -4))
    print(for_loop5(10, 5, 2))

if __name__ == '__main__':
    main()