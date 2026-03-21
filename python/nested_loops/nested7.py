# @desc Both loops start at 1 using **range(1, n + 1)**, so think about what values **i** and **j** take.

def nested7(n):
    result = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result += i * j
    return result


def main():
    print(nested7(3))
    print(nested7(1))
    print(nested7(2))
    print(nested7(4))
    print(nested7(0))


if __name__ == '__main__':
    main()
