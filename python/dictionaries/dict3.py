# @desc The **in** operator checks whether a key exists in a dictionary, regardless of the associated value.

def dict3(d, key):
    return key in d


def main():
    print(dict3({'a': 1}, 'a'))
    print(dict3({'a': 1}, 'b'))
    print(dict3({}, 'x'))
    print(dict3({'x': 0, 'y': 1}, 'y'))
    print(dict3({'a': None}, 'a'))


if __name__ == '__main__':
    main()
