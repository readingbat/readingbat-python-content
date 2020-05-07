def gteq_expr(val1, val2):
    result = val1 >= val2
    return result


def main():
    print(gteq_expr(6, 4))
    print(gteq_expr(12, 12))
    print(gteq_expr(8, 8))
    print(gteq_expr(12, 24))
    print(gteq_expr(7, 2))


if __name__ == "__main__":
    main()
