# @desc Each element is compared with **>** to produce True or False, and the results are collected into a list.

def above_five(vals):
    results = []
    for v in vals:
        results.append(v > 5)
    return results


def main():
    print(above_five([5, 6]))
    print(above_five([6]))


if __name__ == '__main__':
    main()
