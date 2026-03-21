# @desc You can filter strings by their length using **len()** in the **if** condition.

def list_comp8(words, n):
    return [w for w in words if len(w) > n]


def main():
    print(list_comp8(['hi', 'hello', 'a'], 2))
    print(list_comp8(['cat', 'dog'], 3))
    print(list_comp8(['python', 'is', 'fun'], 2))
    print(list_comp8([], 5))


if __name__ == '__main__':
    main()
