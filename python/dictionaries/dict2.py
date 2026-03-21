# @desc The **.get()** method returns the value for a key if it exists, otherwise it returns a default value.

def dict2(d, key):
    return d.get(key, 0)


def main():
    print(dict2({'a': 1, 'b': 2}, 'a'))
    print(dict2({'a': 1}, 'b'))
    print(dict2({}, 'x'))
    print(dict2({'x': 10, 'y': 20}, 'y'))
    print(dict2({'score': 99}, 'score'))


if __name__ == '__main__':
    main()
