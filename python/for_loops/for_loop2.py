def forloop2(x, y):
    z = 0
    for i in range(x):
        z += 1
    return y - z

def main():
    print(forloop2(5, 7))
    print(forloop2(2, 5))
    print(forloop2(1, 8))
    print(forloop2(15, 1))
    print(forloop2(150, 0))
    print(forloop2(10, 10))


if __name__ == '__main__':
    main()
