# @desc Using **d[key]** retrieves the value associated with that key in the dictionary.

def dict1(d, key):
    return d[key]


def main():
    print(dict1({'a': 1, 'b': 2}, 'a'))
    print(dict1({'x': 10, 'y': 20}, 'y'))
    print(dict1({'name': 5, 'age': 15}, 'name'))
    print(dict1({'cats': 3, 'dogs': 7}, 'dogs'))
    print(dict1({'score': 100}, 'score'))


if __name__ == '__main__':
    main()
