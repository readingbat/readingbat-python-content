def concat1(t, s):
    result = ""
    for i in t:
        result+=s
    return result


def main():
    print(concat1(3, "Car"))
    print(concat1(1, "Hello"))
    print(concat1(9, "5"))
    print(concat1(5, "ree"))
    print(concat1(3, "Hi"))
    print(concat1(4, "bat"))
    print(concat1(5, ""))
    print(concat1(4, " "))
    print(concat1(0, "abc"))

if __name__ == "__main__":
    main()