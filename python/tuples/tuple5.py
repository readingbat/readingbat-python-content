# @desc The **+** operator joins two tuples into a new, longer tuple.

def tuple5(t1, t2):
    return str(t1 + t2)


def main():
    print(tuple5((1, 2), (3, 4)))
    print(tuple5(('a',), ('b',)))
    print(tuple5((), (1, 2)))
    print(tuple5((1, 2, 3), ()))


if __name__ == '__main__':
    main()
