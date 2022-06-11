menu = {
    "Baja Taco": 400,
    "Burrito": 750,
    "Bowl": 850,
    "Nachos": 1100,
    "Quesadilla": 850,
    "Super Burrito": 850,
    "Super Quesadilla": 950,
    "Taco": 300,
    "Tortilla Salad": 800
}

total = 0

while True:
    try:
        order = input("Item: ")
        total = int(total) + int(menu[order.title()])
        print("$", f"{total/100:.2f}", sep="")
    except KeyError:
        pass
    except EOFError:
        print("\n")
        break