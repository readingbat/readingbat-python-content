# @desc Which order are the **and** and the **or** evaluated?

def andor7(val1, val2, val3):
    result = val1 or val2 and val3
    return result


def main():
    print(andor7(True, True, True))
    print(andor7(True, True, False))
    print(andor7(True, False, True))
    print(andor7(True, False, False))
    print(andor7(False, True, True))
    print(andor7(False, True, False))
    print(andor7(False, False, True))
    print(andor7(False, False, False))


if __name__ == '__main__':
    main()
