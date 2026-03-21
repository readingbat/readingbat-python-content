# @desc **x % 2 == 0** tests if a number is even. Use this in the **if** part of the comprehension.

def list_comp7(lst):
    return [x for x in lst if x % 2 == 0]


def main():
    print(list_comp7([1, 2, 3, 4, 5, 6]))
    print(list_comp7([1, 3, 5]))
    print(list_comp7([2, 4]))
    print(list_comp7([]))
    print(list_comp7([0, 1]))


if __name__ == '__main__':
    main()
