# @desc The **sorted()** function returns a new sorted list from the items of any iterable, including dictionary keys.

def dict6(d):
    return sorted(d.keys())


def main():
    print(dict6({'b': 1, 'a': 2}))
    print(dict6({'z': 1, 'm': 2, 'a': 3}))
    print(dict6({}))
    print(dict6({'x': 1}))


if __name__ == '__main__':
    main()
