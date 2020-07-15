def forloop3(str):
    result = 0
    for i in str:
        if i == "a":
            result += 1
    return result

def main():
    print(forloop3(["Hello", "world", "a"]))
    print(forloop3(["a", "a"]))
    print(forloop3(["Computational", "thinking"]))
    print(forloop3(["a", "A", "A"]))

if __name__ == '__main__':
    main()