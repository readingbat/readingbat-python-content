# @desc The two loops check every pair of elements at different positions to see if they sum to the target using **return**.

def nested8(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return True
    return False


def main():
    print(nested8([1, 2, 3], 5))
    print(nested8([1, 2, 3], 7))
    print(nested8([1, 1], 2))
    print(nested8([], 5))
    print(nested8([5], 10))
    print(nested8([3, 7, 1, 9], 10))


if __name__ == '__main__':
    main()
