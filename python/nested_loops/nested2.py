# @desc Track the values of **i** and **j** at each step and compute their product before adding to the result.

def nested2(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += i * j
    return result


def main():
    print(nested2(3))
    print(nested2(2))
    print(nested2(1))
    print(nested2(4))
    print(nested2(0))


if __name__ == '__main__':
    main()
