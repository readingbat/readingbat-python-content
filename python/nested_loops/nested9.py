# @desc The nested **for** loops compare every character in the first string against every character in the second string.

def nested9(s, sub):
    result = 0
    for c1 in s:
        for c2 in sub:
            if c1 == c2:
                result += 1
    return result


def main():
    print(nested9('hello', 'lo'))
    print(nested9('aaa', 'a'))
    print(nested9('abc', 'xyz'))
    print(nested9('', 'hello'))
    print(nested9('abab', 'ab'))


if __name__ == '__main__':
    main()
