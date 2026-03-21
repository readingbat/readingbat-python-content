# @desc The inner loop starts after the outer loop index to avoid counting the same pair twice using **range**.

def nested4(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                result += 1
    return result


def main():
    print(nested4([1, 1, 1]))
    print(nested4([1, 2, 3]))
    print(nested4([1, 1]))
    print(nested4([1, 2, 1]))
    print(nested4([]))


if __name__ == '__main__':
    main()
