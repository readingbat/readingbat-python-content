# @desc A comprehension can both filter with **if** and transform the kept elements in the same expression.

def list_comp9(lst):
    return [x + 1 for x in lst if x >= 0]


def main():
    print(list_comp9([1, -2, 3, -4, 0]))
    print(list_comp9([]))
    print(list_comp9([-1, -2]))
    print(list_comp9([0, 1, 2]))
    print(list_comp9([5]))


if __name__ == '__main__':
    main()
