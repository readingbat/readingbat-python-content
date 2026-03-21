# @desc You must convert numbers to strings with **str()** before using **+** to join them with other strings.

def type_conv6(name, age):
    return name + ' is ' + str(age)


def main():
    print(type_conv6('Alice', 25))
    print(type_conv6('Bob', 0))
    print(type_conv6('Eve', 100))
    print(type_conv6('', 5))


if __name__ == '__main__':
    main()
