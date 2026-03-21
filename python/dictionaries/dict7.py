# @desc The **sorted()** function can sort **d.values()** into a list in ascending order.

def dict7(d):
    return sorted(d.values())


def main():
    print(dict7({'a': 3, 'b': 1, 'c': 2}))
    print(dict7({'x': 10}))
    print(dict7({}))
    print(dict7({'a': 5, 'b': 5}))


if __name__ == '__main__':
    main()
