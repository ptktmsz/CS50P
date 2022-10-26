import csv
import sys
from tabulate import tabulate

prices = []

if len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            print(reader.fieldnames[1])
            for row in reader:
                prices.append({reader.fieldnames[0]: row[reader.fieldnames[0]], reader.fieldnames[1]: row[reader.fieldnames[1]], reader.fieldnames[2]: row[reader.fieldnames[2]]})
        print(tabulate(prices, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")