# @desc Removing leading characters using a **while** loop with string slicing. The loop checks the first character each time.

def while_loop8(s, c):
    while len(s) > 0 and s[0] == c:
        s = s[1:]
    return s


def main():
    print(while_loop8('aaahello', 'a'))
    print(while_loop8('xxxy', 'x'))
    print(while_loop8('hello', 'a'))
    print(while_loop8('aaa', 'a'))
    print(while_loop8('', 'x'))


if __name__ == '__main__':
    main()
