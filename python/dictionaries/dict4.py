# @desc A **for** loop can build a dictionary by counting how many times each character appears in a string.

def dict4(s):
    counts = {}
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return str(counts)


def main():
    print(dict4('aab'))
    print(dict4('hello'))
    print(dict4(''))
    print(dict4('aaa'))


if __name__ == '__main__':
    main()
