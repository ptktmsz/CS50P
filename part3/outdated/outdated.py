months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


def main():

    while True:
        userdate = input("Date: ")
        try:
            medtoiso(userdate)
            break
        except ValueError:
            try:
                mewtoiso(userdate)
                break
            except ValueError:
                pass


# middle-endian digits to iso
def medtoiso(meddate):
    medm, medd, medy = meddate.split("/")
    if " " in medy or " " in medm or " " in medd:
        raise ValueError
    elif int(medy) >= 0 and 0 < int(medm) < 13 and 0 < int(medd) < 32:
        print(f"{int(medy):04}-{int(medm):02}-{int(medd):02}")
    else:
        raise ValueError


# middle-endian words to iso
def mewtoiso(mewdate):
    mewm, mewd, mewy = mewdate.split(" ")
    cmewd = int(mewd.replace(",",""))
    cmewm = mewm.title()
    cmewy = int(mewy)
    if cmewy >= 0 and cmewm in months.keys() and 0 < cmewd < 32 and "," in mewd:
        print(f"{cmewy:04}-{int(months[cmewm]):02}-{cmewd:02}")
    else:
        raise ValueError


main()