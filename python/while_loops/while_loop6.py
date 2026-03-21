# @desc Repeatedly halving a number using **//2** and counting the steps. The loop stops when the value reaches 1 or less.

def while_loop6(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count


def main():
    print(while_loop6(8))
    print(while_loop6(1))
    print(while_loop6(16))
    print(while_loop6(10))
    print(while_loop6(100))
    print(while_loop6(2))


if __name__ == '__main__':
    main()
