# @desc A slice is inclusive of the starting index and exclusive of the ending index.

def slice4(s):
    c = s[0:2]
    return c


def main():
    print(slice4('Car'))
    print(slice4('Truck'))
    print(slice4('556843'))
    print(slice4('Elephant'))
    print(slice4('Roses'))


if __name__ == '__main__':
    main()
