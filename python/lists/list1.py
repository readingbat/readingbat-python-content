# @desc **range(x)** generates numbers from 0 up to (but not including) **x**.

def list1(x):
    result = 0
    for i in range(x):
        result += 2
    return result


def main():
    print(list1(5))
    print(list1(2))
    print(list1(1))
    print(list1(15))
    print(list1(150))
    print(list1(10))


if __name__ == '__main__':
    main()
