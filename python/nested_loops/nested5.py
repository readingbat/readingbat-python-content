# @desc Notice the inner loop runs **range(i + 1)** times, so it grows with each iteration of the outer loop.

def nested5(s, n):
    result = ''
    for i in range(n):
        for j in range(i + 1):
            result += s
    return result


def main():
    print(nested5('a', 3))
    print(nested5('x', 1))
    print(nested5('hi', 2))
    print(nested5('a', 0))


if __name__ == '__main__':
    main()
