def above_five(vals):
    results = []
    for v in vals:
        if (v > 5):
            results.append('a')
        else:
            results.append('b')
    return results


def main():
    print(above_five([5, 6]))
    print(above_five([6]))


if __name__ == '__main__':
    main()
