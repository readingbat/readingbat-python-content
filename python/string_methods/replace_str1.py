# @desc **.replace()** swaps every occurrence of a substring, not just the first.

def replace_str1(s, old, new):
    return s.replace(old, new)


def main():
    print(replace_str1('hello world', 'world', 'there'))
    print(replace_str1('aaa', 'a', 'b'))
    print(replace_str1('hello', 'x', 'y'))
    print(replace_str1('abab', 'ab', 'x'))
    print(replace_str1('', ' ', 'x'))


if __name__ == '__main__':
    main()
