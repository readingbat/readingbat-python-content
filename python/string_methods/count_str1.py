# @desc **.count()** returns how many times a substring appears without overlapping.

def count_str1(s, sub):
    return s.count(sub)


def main():
    print(count_str1('hello', 'l'))
    print(count_str1('aaa', 'a'))
    print(count_str1('hello', 'x'))
    print(count_str1('hello', 'll'))
    print(count_str1('banana', 'an'))
    print(count_str1('', ' '))


if __name__ == '__main__':
    main()
