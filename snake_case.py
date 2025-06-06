# camelCase to snake_case

# Input
def main():
    print("\n")
    camel = input("camelCase: ")
    snake = ""

    for c in camel:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c

    print(f"snake_case: {snake}")

if __name__ == "__main__":
    main() 




