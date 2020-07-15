def forloop5(x, y, z):
    result = []
    for i in range(x, y, z):
        result.append(i)
    return result

def main():
    print(forloop5(0, 5, 2))
    print(forloop5(10, 5, -1))
    print(forloop5(20, 0, -4))
    print(forloop5(10, 5, 2))

if __name__ == '__main__':
    main()