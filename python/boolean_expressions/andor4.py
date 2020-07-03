def andor4(val1, val2):
    result = not (val1 or val2)
    return result


def main():
    print(andor4(True, True))
    print(andor4(True, False))
    print(andor4(False, True))
    print(andor4(False, False))


if __name__ == '__main__':
    main()
