def for_loop4(str, x):
    result = 0
    for i in str[x:]:
        if i == "a":
            result += 1
    return result


def main():
    print(for_loop4(["Hello", "world", "a"], 2))
    print(for_loop4(["a", "a"], 0))
    print(for_loop4(["a", "a"], 1))
    print(for_loop4(["Computational", "thinking"], 1))
    print(for_loop4(["a", "A", "A"], 1))

if __name__ == '__main__':
    main()