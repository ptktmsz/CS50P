import csv
import sys

def main():
    checkargvs()
    rewrite()

def checkargvs():
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a CSV file")
    elif sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a CSV file")

def rewrite():
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            with open(sys.argv[2], "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    lastname, firstname = row[reader.fieldnames[0]].split(",")
                    writer.writerow({"first":firstname.strip(), "last":lastname.strip(), "house":row[reader.fieldnames[1]]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

main()