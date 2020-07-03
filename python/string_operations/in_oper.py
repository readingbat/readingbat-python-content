def in_oper(s1, s2):
    result = s1 in s2
    return result


def main():
    print(in_oper('e', 'Hello'))
    print(in_oper('g', 'Hello'))
    print(in_oper('2', '525'))
    print(in_oper('74', '525'))
    print(in_oper('gg', 'Egg'))
    print(in_oper('', 'World'))
    print(in_oper(' ', 'Hello World'))
    print(in_oper(' ', 'HelloWorld'))


if __name__ == '__main__':
    main()
