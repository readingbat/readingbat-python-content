# @desc Counting digits by repeatedly dividing by 10 using **//** (integer division). Consider the special case when the number is 0.

def while_loop5(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


def main():
    print(while_loop5(123))
    print(while_loop5(0))
    print(while_loop5(9))
    print(while_loop5(9999))
    print(while_loop5(10))
    print(while_loop5(1000000))


if __name__ == '__main__':
    main()
