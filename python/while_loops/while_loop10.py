# @desc Shrinking a string by removing the first and last characters with slicing inside a **while** loop. Think about when the loop stops.

def while_loop10(s):
    while len(s) > 2:
        s = s[1:-1]
    return s


def main():
    print(while_loop10('hello'))
    print(while_loop10('abcdef'))
    print(while_loop10('ab'))
    print(while_loop10('x'))
    print(while_loop10('abcdefgh'))
    print(while_loop10('abc'))


if __name__ == '__main__':
    main()
