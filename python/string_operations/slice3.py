# @desc The first character in a string is at index 0.

def slice3(s):
    length = len(s)
    mid = int(length / 2)
    c = s[mid]
    return c


def main():
    print(slice3('Car'))
    print(slice3('Truck'))
    print(slice3('556843'))
    print(slice3('Elephant'))
    print(slice3('Roses'))


if __name__ == '__main__':
    main()
