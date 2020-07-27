# @desc Truth tables

def andor1(val1, val2):
    result = val1 and val2
    return result


def main():
    print(andor1(True, True))
    print(andor1(True, False))
    print(andor1(False, True))
    print(andor1(False, False))


if __name__ == '__main__':
    main()
