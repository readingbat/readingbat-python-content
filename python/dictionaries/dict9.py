# @desc The **update()** method merges one dictionary into another, with later updates overwriting earlier keys.

def dict9(d1, d2):
    d = {}
    d.update(d1)
    d.update(d2)
    return len(d)


def main():
    print(dict9({'a': 1}, {'b': 2}))
    print(dict9({'a': 1}, {'a': 2}))
    print(dict9({}, {}))
    print(dict9({'a': 1, 'b': 2}, {'c': 3}))


if __name__ == '__main__':
    main()
