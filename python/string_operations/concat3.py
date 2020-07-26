# @desc Print a string a certain number of times.

def concat3(t, s):
    result = ''
    for i in range(t):
        result += s
    return result


def main():
    print(concat3(3, 'Car'))
    print(concat3(1, 'Hello'))
    print(concat3(9, '5'))
    print(concat3(5, 'ree'))
    print(concat3(3, 'Hi'))
    print(concat3(4, 'bat'))
    print(concat3(5, ''))
    print(concat3(4, ' '))
    print(concat3(0, 'abc'))


if __name__ == '__main__':
    main()
