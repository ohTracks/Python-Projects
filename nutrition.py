# program that outputs the amount of calories of a certain fruit
# ask for fruit in input and return calories

# user input
k = input("Fruit: ").lower().strip()

# create dict
fruits = {
    "apple": "130 calories",
    "avocado": "50 calories",
    "banana": "110 calories",
    "grapes": "90 calories",
    "melon": "50 calories",
    "kiwi": "90 calories",
    "lime": "20 calories",
    "orange": "80 calories",
    "peach": "60 calories",
    "pear": "100 calories",
    "pineapple": "50 calories",
    "strawberries": "50 calories",
    "watermelon": "80 calories",
}

# return calories and ignore != fruit
for _ in fruits:
    if k in fruits:
        print(k.capitalize(), fruits[k], sep=", ")
        break
    else:
        break