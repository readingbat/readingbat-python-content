def split(out, word):
    length = int(len(out)/2)
    return out[:length] + word + out[length:]

def main():
    print(split('Hello', 'World'))
    print(split('Person', 'a'))
    print(split('Alpha', 'Omega'))
    print(split('Rain', 'boots'))
    print(split('School', 'bus'))
    print(split('', 'Hi'))
    print(split('Matt', ''))
    print(split('5', '8'))

if __name__ == '__main__':
    main()