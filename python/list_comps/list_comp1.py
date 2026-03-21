# @desc A list comprehension **[x for x in lst]** creates a new list by visiting each element.

def list_comp1(lst):
    return [str(x) for x in lst]


def main():
    print(list_comp1([1, 2, 3]))
    print(list_comp1([]))
    print(list_comp1(['a', 'b']))
    print(list_comp1([True]))


if __name__ == '__main__':
    main()
