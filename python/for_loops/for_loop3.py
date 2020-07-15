def for_loop3(str):
    result = 0
    for i in str:
        if i == "a":
            result += 1
    return result


def main():
    print(for_loop3(["Hello", "world", "a"]))
    print(for_loop3(["a", "a"]))
    print(for_loop3(["Computational", "thinking"]))
    print(for_loop3(["a", "A", "A"]))


if __name__ == '__main__':
    main()
