def andor2(val1, val2):
    result = val1 or val2
    return result


def main():
    print(andor2(True, True))
    print(andor2(True, False))
    print(andor2(False, True))
    print(andor2(False, False))


if __name__ == '__main__':
    main()
