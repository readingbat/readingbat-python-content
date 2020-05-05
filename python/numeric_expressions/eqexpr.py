def eqexpr(val1, val2):
    result = val1 == val2
    return result


def main():
    print(eqexpr(6, 6))
    print(eqexpr(12, 12))
    print(eqexpr(8, 7))
    print(eqexpr(12, 24))
    print(eqexpr(7, 7))


if __name__ == "__main__":
    main()
