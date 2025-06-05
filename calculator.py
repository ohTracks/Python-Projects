while True:
    op = input("Select your operator: (+, -, *, / , p, E to Exit) ")

    if op == "E":
        break
    
    n1 = int(input("First number: "))
    n2 = int(input("Second number: "))

    if op == "+":
        print(n1 + n2)
    elif op == "-":
        print(n1 - n2)
    elif op == "*":
        print(n1 * n2)
    elif op == "/":
        if n2 == 0:
            print("Error: Division by zero!")
        else:
            print(n1 / n2)
    elif op == "p":
        print(pow(n1, n2))
    else:
        print("Enter a valid operation!")
