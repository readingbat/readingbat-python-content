def list4(str, x):
    result = 0
    for i in str[x:]:
        if i == 'a':
            result += 1
    return result


def main():
    print(list4(['Hello', 'world', 'a'], 2))
    print(list4(['a', 'a'], 0))
    print(list4(['a', 'a'], 1))
    print(list4(['Computational', 'thinking'], 1))
    print(list4(['a', 'A', 'A'], 1))

if __name__ == '__main__':
    main()