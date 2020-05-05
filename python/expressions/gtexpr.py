def gtexpr(val1, val2):
    result = val1 > val2
    return result


def main():
    print(gtexpr(4, 6))
    print(gtexpr(8, 12))
    print(gtexpr(19, 19))
    print(gtexpr(12, 8))
    print(gtexpr(11, 28))


if __name__ == "__main__":
    main()
