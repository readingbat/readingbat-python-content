def count1(x):
    count = 0
    for i in range(len(x)):
        if x[i:i+2] == 'ba':
            count+=1
    return count

def main():
    print(count1('baba'))
    print(count1('aba'))
    print(count1('baaabab'))
    print(count1('abc'))
    print(count1('goodbye'))
    print(count1('a'))
    print(count1('ba'))

if __name__ == '__main__':
    main()