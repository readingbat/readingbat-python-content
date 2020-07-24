# @desc This is a description of **boolean_list**

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