# @desc The **endswith()** function returns True if a string ends with a specified substring.

def ends_with(s1, s2):
    result = s2.endswith(s1)
    return result


def main():
    print(ends_with('o', 'Hello'))
    print(ends_with('ll', 'Hello'))
    print(ends_with('llo', 'Hello'))
    print(ends_with('5', '525'))
    print(ends_with('52', '525'))
    print(ends_with('25', '525'))
    print(ends_with('g', 'Egg'))
    print(ends_with('', 'World'))
    print(ends_with(' ', 'Hello World '))
    print(ends_with(' ', 'HelloWorld'))


if __name__ == '__main__':
    main()
