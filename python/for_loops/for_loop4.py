def for_loop4(str, x):
    result = 0
    for i in str:
        if i == x:
            result += 1
    return result

def main():
    print(for_loop4('athenian', 'e'))
    print(for_loop4('apples', 'a'))
    print(for_loop4('hello', 'a'))
    print(for_loop4('alphabet', 'h'))
    print(for_loop4('aaaaa', 'b'))

if __name__ == '__main__':
    main()