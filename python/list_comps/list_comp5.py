# @desc You can apply any function like **len()** to each element inside a list comprehension.

def list_comp5(words):
    return [len(w) for w in words]


def main():
    print(list_comp5(['hi', 'hello', 'a']))
    print(list_comp5([]))
    print(list_comp5(['']))
    print(list_comp5(['cat', 'dog']))
    print(list_comp5(['python']))


if __name__ == '__main__':
    main()
