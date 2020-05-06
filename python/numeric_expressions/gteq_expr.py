def gteqexpr(val1, val2):
    result = val1 >= val2
    return result


def main():
    print(gteqexpr(6, 4))
    print(gteqexpr(12, 12))
    print(gteqexpr(8, 8))
    print(gteqexpr(12, 24))
    print(gteqexpr(7, 2))


if __name__ == "__main__":
    main()
