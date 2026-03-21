# @desc The **len()** function returns the number of key-value pairs in a dictionary.

def dict8(d):
    return len(d)


def main():
    print(dict8({'a': 1, 'b': 2}))
    print(dict8({}))
    print(dict8({'x': 1}))
    print(dict8({'a': 1, 'b': 2, 'c': 3, 'd': 4}))


if __name__ == '__main__':
    main()
