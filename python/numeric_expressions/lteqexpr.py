def lteqexpr(val1, val2):
    result = val1 <= val2
    return result


def main():
    print(lteqexpr(6, 4))
    print(lteqexpr(12, 12))
    print(lteqexpr(8, 8))
    print(lteqexpr(12, 24))
    print(lteqexpr(7, 2))


if __name__ == "__main__":
    main()
