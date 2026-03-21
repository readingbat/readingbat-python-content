# @desc Think about how many times the inner loop runs for each iteration of the outer loop using **range**.

def nested1(x, y):
    result = 0
    for i in range(x):
        for j in range(y):
            result += 1
    return result


def main():
    print(nested1(3, 4))
    print(nested1(2, 2))
    print(nested1(0, 5))
    print(nested1(5, 0))
    print(nested1(1, 1))
    print(nested1(3, 3))


if __name__ == '__main__':
    main()
