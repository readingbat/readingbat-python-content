# @desc Consider how the outer loop controls rows and the inner loop controls columns using **range**.

def nested3(rows, cols):
    result = 0
    for i in range(rows):
        for j in range(cols):
            result += 1
    return result


def main():
    print(nested3(2, 3))
    print(nested3(1, 1))
    print(nested3(0, 5))
    print(nested3(4, 4))


if __name__ == '__main__':
    main()
