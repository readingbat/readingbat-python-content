# @desc The **not** operator flips True to False and False to True. Trace which branch the **if** takes.

def simple_choice1(sunny):
    if (not sunny):
        return sunny
    else:
        return not sunny


def main():
    print(simple_choice1(True))
    print(simple_choice1(False))


if __name__ == '__main__':
    main()
