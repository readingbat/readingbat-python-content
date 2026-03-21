# @desc The **if/else** inside the loop appends **1** or **0** depending on whether each value passes the test.

def above_five(vals):
    results = []
    for v in vals:
        if (v > 5):
            results.append(1)
        else:
            results.append(0)
    return results


def main():
    print(above_five([5, 6]))
    print(above_five([6]))


if __name__ == '__main__':
    main()
