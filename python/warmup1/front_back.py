
def front_back(s):
    if (len(s) < 2):
        return s
    f = s[0]
    e = s[-1]
    return e + f


def main():
    print(front_back("This is a test"))
    print(front_back(""))
    print(front_back("t"))


if __name__ == "__main__":
    main()