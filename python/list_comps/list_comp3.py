# @desc Adding **if** at the end of a list comprehension keeps only elements that pass the test.

def list_comp3(lst):
    return [x for x in lst if x > 0]


def main():
    print(list_comp3([1, -2, 3, -4, 5]))
    print(list_comp3([]))
    print(list_comp3([-1, -2]))
    print(list_comp3([0, 1, 2]))
    print(list_comp3([5]))


if __name__ == '__main__':
    main()
