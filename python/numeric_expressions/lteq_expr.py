def lteq_expr(val1, val2):
    result = val1 <= val2
    return result


def main():
    print(lteq_expr(6, 4))
    print(lteq_expr(12, 12))
    print(lteq_expr(8, 8))
    print(lteq_expr(12, 24))
    print(lteq_expr(7, 2))


if __name__ == "__main__":
    main()
