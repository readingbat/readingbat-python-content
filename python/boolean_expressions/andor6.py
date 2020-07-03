def andor6(val1, val2, val3):
    result = val1 and (val2 or val3)
    return result


def main():
    print(andor6(True, True, True))
    print(andor6(True, True, False))
    print(andor6(True, False, True))
    print(andor6(True, False, False))
    print(andor6(False, True, True))
    print(andor6(False, True, False))
    print(andor6(False, False, True))
    print(andor6(False, False, False))


if __name__ == "__main__":
    main()
