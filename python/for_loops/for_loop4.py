def for_loop3(str, x):
    result = 0
    for i in str:
        if i == x:
            result += 1
    return result

def main():
    print(for_loop3('athenian', 'e'))
    print(for_loop3('apples', 'a'))
    print(for_loop3('hello', 'a'))
    print(for_loop3('alphabet', 'h'))
    print(for_loop3('aaaaa', 'b'))

if __name__ == '__main__':
    main()