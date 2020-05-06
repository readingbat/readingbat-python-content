def gt_expr(val1, val2):
    result = val1 > val2
    return result


def main():
    print(gt_expr(4, 6))
    print(gt_expr(8, 12))
    print(gt_expr(19, 19))
    print(gt_expr(12, 8))
    print(gt_expr(11, 28))


if __name__ == "__main__":
    main()
