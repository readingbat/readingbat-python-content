def andor5(val1, val2, val3):
    result = val1 or val2 and val3
    return result


def main():
    print(andor5(True, True, True))
    print(andor5(True, True, False))
    print(andor5(True, False, True))
    print(andor5(True, False, False))
    print(andor5(False, True, True))
    print(andor5(False, True, False))
    print(andor5(False, False, True))
    print(andor5(False, False, False))


if __name__ == '__main__':
    main()
