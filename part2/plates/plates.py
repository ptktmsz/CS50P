def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if strlength(s) == False:
        return False

    elif strstart(s) == False:
        return False

    elif numbersend(s) == False:
        return False

    elif numbernotzero(s) == False:
        return False

    elif noperiods(s) == False:
        return False

    else:
        return True

# DONE checks for number of characters on a plate (valid is between 2 and 6)
def strlength(s):
    if len(s) > 6 or len(s) < 2:
        return False
    return True

# DONE checks if plate starts with at least two letters
def strstart(s):
    if s[0:1].isdigit() == True:
        return False
    elif s[1:2].isdigit() == True:
        return False
    else:
        return True

# checks if numbers come at the end - cannot be used in the middle
def numbersend(s):
    for c in s:
        if c.isnumeric() == True:
            firstnumber = c
            if s[s.index(firstnumber):len(s)].isnumeric() == True:
                return True
            else:
                return False

# checks if numbers start with something else than a 0
def numbernotzero(s):
    for c in s:
        if c.isnumeric() == True:
            firstnumber = c
            if s[s.index(firstnumber):len(s)].startswith("0") == True:
                return False
            else:
                return True


# checks if no periods, spaces, or punctuation marks are used
def noperiods(s):
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    for c in s:
        if c in punctuation:
            return False
    return True

main()