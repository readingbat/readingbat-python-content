# @desc A value is doubled repeatedly until it exceeds a **limit**. Track the value after each doubling step.

def while_loop4(x, limit):
    while x <= limit:
        x *= 2
    return x


def main():
    print(while_loop4(1, 10))
    print(while_loop4(1, 100))
    print(while_loop4(3, 50))
    print(while_loop4(5, 5))
    print(while_loop4(1, 1))


if __name__ == '__main__':
    main()
