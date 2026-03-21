# @desc The **sum()** function can be applied to **d.values()** to add up all the values in a dictionary.

def dict5(d):
    return sum(d.values())


def main():
    print(dict5({'a': 1, 'b': 2, 'c': 3}))
    print(dict5({'x': 10}))
    print(dict5({}))
    print(dict5({'a': -1, 'b': 5}))


if __name__ == '__main__':
    main()
