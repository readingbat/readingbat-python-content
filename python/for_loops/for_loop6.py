def for_loop6(str, x):
    result = 0
    xl = len(x)
    for i in range(len(str)-xl+1):
        if str[i: i + xl] == x:
            result += 1
    return result

def main():
    print(for_loop6('athenian', 'e'))
    print(for_loop6('apples', 'ap'))
    print(for_loop6('hello', 'a'))
    print(for_loop6('alphabet', 'al'))
    print(for_loop6('aaaaa', 'aa'))

if __name__ == '__main__':
    main()