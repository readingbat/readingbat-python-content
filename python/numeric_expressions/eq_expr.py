def eq_expr(val1, val2):
    result = val1 == val2
    return result


def main():
    print(eq_expr(6, 6))
    print(eq_expr(12, 12))
    print(eq_expr(8, 7))
    print(eq_expr(12, 24))
    print(eq_expr(7, 7))


if __name__ == "__main__":
    main()
