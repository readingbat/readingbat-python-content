def andor3(val1, val2):
    result = not (val1 and val2)
    return result


def main():
    print(andor3(True, True))
    print(andor3(True, False))
    print(andor3(False, True))
    print(andor3(False, False))


if __name__ == '__main__':
    main()
