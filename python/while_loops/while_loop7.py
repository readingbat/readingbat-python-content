# @desc Building a string by using **+=** to append inside a **while** loop. Track the counter and the growing result.

def while_loop7(s, n):
    result = ''
    i = 0
    while i < n:
        result += s
        i += 1
    return result


def main():
    print(while_loop7('ab', 3))
    print(while_loop7('x', 0))
    print(while_loop7('hi', 1))
    print(while_loop7('!', 5))


if __name__ == '__main__':
    main()
