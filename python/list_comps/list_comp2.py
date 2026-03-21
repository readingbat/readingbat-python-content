# @desc You can transform each element in a list comprehension by applying an expression before the **for**.

def list_comp2(lst):
    return [x * 2 for x in lst]


def main():
    print(list_comp2([1, 2, 3]))
    print(list_comp2([0, 5]))
    print(list_comp2([]))
    print(list_comp2([10]))
    print(list_comp2([-1, 1]))


if __name__ == '__main__':
    main()
