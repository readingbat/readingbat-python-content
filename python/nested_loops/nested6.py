# @desc For each element in the first list, the inner loop checks every element in the second list using **for** and **if**.

def nested6(a, b):
    result = 0
    for x in a:
        for y in b:
            if x == y:
                result += 1
    return result


def main():
    print(nested6([1, 2, 3], [2, 3, 4]))
    print(nested6([1, 1], [1]))
    print(nested6([], [1, 2]))
    print(nested6([1, 2], [3, 4]))
    print(nested6([5], [5]))


if __name__ == '__main__':
    main()
