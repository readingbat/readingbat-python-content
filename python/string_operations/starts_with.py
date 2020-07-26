# @desc **startswith()** returns True if a string starts with a specified substring.

def starts_with(s1, s2):
    result = s2.startswith(s1)
    return result


def main():
    print(starts_with('H', 'Hello'))
    print(starts_with('el', 'Hello'))
    print(starts_with('Hel', 'Hello'))
    print(starts_with('5', '525'))
    print(starts_with('52', '525'))
    print(starts_with('25', '525'))
    print(starts_with('E', 'Egg'))
    print(starts_with('', 'World'))
    print(starts_with(' ', ' Hello World'))
    print(starts_with(' ', 'HelloWorld'))


if __name__ == '__main__':
    main()
