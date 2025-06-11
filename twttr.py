def main():
    msg = input("input: ")
    print (rVowels(msg))

def rVowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    fstring = ''.join([char for char in string if char not in vowels])
    return(fstring)

main()