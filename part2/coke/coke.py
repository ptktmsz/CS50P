due = 50

while due > 0:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin

if due <= 0:
    print(f"Change Owed: {abs(due)}")
