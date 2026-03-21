# @desc **range(n)** generates numbers from 0 to n-1, and __**2__ squares each one.

def list_comp6(n):
    return [i**2 for i in range(n)]


def main():
    print(list_comp6(5))
    print(list_comp6(0))
    print(list_comp6(1))
    print(list_comp6(3))
    print(list_comp6(4))


if __name__ == '__main__':
    main()
