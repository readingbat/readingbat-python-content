# @desc A countdown subtracts 2 each step. Think about whether the final value lands exactly on 0 or goes past it.

def while_loop3(n):
    while n > 0:
        n -= 2
    return n


def main():
    print(while_loop3(10))
    print(while_loop3(7))
    print(while_loop3(1))
    print(while_loop3(4))
    print(while_loop3(5))
    print(while_loop3(0))


if __name__ == '__main__':
    main()
