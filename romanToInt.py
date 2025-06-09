def main():
    r = input("Enter a Roman numeral: ").strip().upper()
    roman_to_int(r)

def roman_to_int(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    rr = 0
    
    for char in reversed(s):
        value = roman_numerals.get(char, 0)
        
        if value < rr:
            total -= value
        else:
            total += value
            
        rr = value
    
    print(total)

main()

