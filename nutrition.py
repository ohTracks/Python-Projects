
k = input("Fruit: ").lower().strip()

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

for _ in fruits:
    if k in fruits:
        print(k.capitalize(), fruits[k], sep=", ")
        break
    else:
        break