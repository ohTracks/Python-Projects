print("Palindrome checker")

def is_palindrome():
    try:
        num = int(input("Enter a number: "))
        num_str = str(num) 

        if num_str == num_str[::-1]:
            print("True")
        else:
            print("False")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

is_palindrome()