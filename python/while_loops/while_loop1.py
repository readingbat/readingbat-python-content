# @desc A **while** loop counts up from 0. Think about when the loop condition becomes **False**.

def while_loop1(n):
    count = 0
    while count < n:
        count += 1
    return count


def main():
    print(while_loop1(5))
    print(while_loop1(0))
    print(while_loop1(1))
    print(while_loop1(10))
    print(while_loop1(3))


if __name__ == '__main__':
    main()
