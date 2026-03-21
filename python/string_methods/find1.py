# @desc **.find()** returns the index where a substring first appears, or **-1** if not found.

def find1(s, sub):
    return s.find(sub)


def main():
    print(find1('hello', 'ell'))
    print(find1('hello', 'x'))
    print(find1('hello', 'lo'))
    print(find1('hello', 'hello'))
    print(find1('aaa', 'a'))
    print(find1('', ' '))


if __name__ == '__main__':
    main()
