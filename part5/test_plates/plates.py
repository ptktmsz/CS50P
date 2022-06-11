import string

def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # checks for number of characters on a plate (valid is between 2 and 6)
    if len(s) > 6 or len(s) < 2:
        return False

    # checks if plate starts with at least two letters
    elif s[0:1].isdigit() == True:
        return False
    elif s[1:2].isdigit() == True:
        return False

    # checks if numbers come at the end - cannot be used in the middle
    for c in s:
        if c.isnumeric() == True:
            firstnumber = c
            if s[s.index(firstnumber):len(s)].isnumeric() == False:
                return False

    # checks if numbers start with something else than a 0
    for c in s:
        if c.isnumeric() == True:
            firstnumber = c
            if s[s.index(firstnumber):len(s)].startswith("0") == True:
                return False

    # checks if no periods, spaces, or punctuation marks are used
    for c in s:
        if c in string.punctuation or c in string.whitespace:
            return False

    else:
        return True


if __name__ == "__main__":
    main()