# @desc A nested **for** in a list comprehension reads left to right — the outer loop runs first, then the inner loop for each element.

def list_comp10(lst):
    return [x for pair in lst for x in pair]


def main():
    print(list_comp10([(1, 2), (3, 4)]))
    print(list_comp10([('a', 'b')]))
    print(list_comp10([]))
    print(list_comp10([(1, 2), (3, 4), (5, 6)]))


if __name__ == '__main__':
    main()
