# @desc An accumulator variable collects a running **sum** inside a **while** loop. Track both the counter and the total.

def while_loop2(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def main():
    print(while_loop2(5))
    print(while_loop2(1))
    print(while_loop2(3))
    print(while_loop2(10))
    print(while_loop2(0))


if __name__ == '__main__':
    main()
