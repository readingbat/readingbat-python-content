def neqexpr(val1, val2):
    result = val1 != val2
    return result


def main():
    print(neqexpr(9, 9))
    print(neqexpr(22, 22))
    print(neqexpr(8, 7))
    print(neqexpr(12, 24))
    print(neqexpr(6, 4))


if __name__ == "__main__":
    main()
