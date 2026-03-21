# @desc Looping over **d.items()** gives key-value pairs that can be swapped to invert a dictionary.

def dict10(d):
    result = {}
    for k, v in d.items():
        result[v] = k
    return str(result)


def main():
    print(dict10({'a': 1, 'b': 2}))
    print(dict10({1: 'x'}))
    print(dict10({}))
    print(dict10({'hello': 'world'}))


if __name__ == '__main__':
    main()
