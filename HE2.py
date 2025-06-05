# Harvard exercise number 2
# Greeting Hello = $0
# Greeting starts with 'h' = $20
# No H in greeting = $100

# Ask user for greeting

print("\n")
g = input("Greeting: ")

# Analise greeting for reward

g = g.lower()

g.find("h")

if g == "hello":
    print("$0")
    exit(0)
elif g.find("h") == 0:
    print("$20")
else:
    print("$100")

exit(0)
