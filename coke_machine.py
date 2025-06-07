d = 50

print(f"Amount due: {d}")

c = int(input("We only accept coins of 25, 10 and 5 cents.\nInsert coins: "))

if c != 25 and c != 10 and c != 5:
    c = int(input(f"Amount due: {d}\nPlease insert a valid coin: "))
        
    
while c < d:
    print(f"Amount due: {d - c}")
    c += int(input("Insert coins: "))

print(f"Change owed: {c - d}")

exit(0)
