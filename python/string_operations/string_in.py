def string_in(s1, s2):
    result = s1 in s2
    return result


def main():
    print(string_in('e', 'Hello'))
    print(string_in('g', 'Hello'))
    print(string_in('2', '525'))
    print(string_in('74', '525'))
    print(string_in('gg', 'Egg'))
    print(string_in('', 'World'))
    print(string_in(' ', 'Hello World'))
    print(string_in(' ', 'HelloWorld'))


if __name__ == '__main__':
    main()
