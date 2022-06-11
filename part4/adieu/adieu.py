names = []

import inflect

p = inflect.engine()

while True:
    try:
        # Add names to the list
        names.append(input("Name: "))
    except EOFError:
        # when ctrl+d pressed, breaks and prints the names
        print("Adieu, adieu, to ", p.join(names), sep="")
        break