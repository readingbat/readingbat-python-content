def for_loop3(str, x):
    result = 0
    xl = len(x)
    for i in range(len(str)-xl+1):
        if str[i: i + xl] == x:
            result += 1
    return result

def main():
    print(for_loop3('athenian', 'e'))
    print(for_loop3('apples', 'ap'))
    print(for_loop3('hello', 'a'))
    print(for_loop3('alphabet', 'al'))
    print(for_loop3('aaaaa', 'aa'))

if __name__ == '__main__':
    main()