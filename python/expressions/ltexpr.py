def ltexpr(val1, val2):
    result = val1 < val2
    return result


def main():
    print(ltexpr(4, 6))
    print(ltexpr(8, 12))
    print(ltexpr(19, 19))
    print(ltexpr(12, 8))
    print(ltexpr(11, 28))


if __name__ == "__main__":
    main()
