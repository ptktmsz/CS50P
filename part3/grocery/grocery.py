items = {

}

while True:
    try:
        item = input().lower()
        if item not in items:
            items[item] = 1
        else:
            items[item] = items.get(item) + 1
    except EOFError:
        for item in sorted(items):
            print(items[item], item.upper())
        break