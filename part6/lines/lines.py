import sys

lines = 0

if len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#") == False and line.strip() != "":
                    lines = lines + 1
            print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")
