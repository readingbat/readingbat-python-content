def list3(strs):
    result = 0
    for i in strs:
        if i == 'a':
            result += 1
    return result


def main():
    print(list3(['Hello', 'world', 'a']))
    print(list3(['a', 'a']))
    print(list3(['Computational', 'thinking']))
    print(list3(['a', 'A', 'A']))


if __name__ == '__main__':
    main()
