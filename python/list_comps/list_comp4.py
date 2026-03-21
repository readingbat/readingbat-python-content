# @desc List comprehensions can call methods like **.upper()** on each element as they build the list.

def list_comp4(words):
    return [w.upper() for w in words]


def main():
    print(list_comp4(['hello', 'world']))
    print(list_comp4(['a']))
    print(list_comp4([]))
    print(list_comp4(['Hi', 'There']))


if __name__ == '__main__':
    main()
