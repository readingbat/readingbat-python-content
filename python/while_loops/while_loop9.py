# @desc Counting even numbers using the **%** (modulo) operator inside a **while** loop. Remember that even numbers have no remainder when divided by 2.

def while_loop9(n):
    count = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            count += 1
        i += 1
    return count


def main():
    print(while_loop9(10))
    print(while_loop9(1))
    print(while_loop9(2))
    print(while_loop9(7))
    print(while_loop9(0))
    print(while_loop9(20))


if __name__ == '__main__':
    main()
