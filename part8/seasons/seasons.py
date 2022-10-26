from datetime import date
import re
import sys
import inflect


def main():
    user_date = input("Date of Birth: ")
    today_date = date.today()
    if validate_date(user_date):
        year, month, day = user_date.split("-")
        user_date = date(int(year), int(month), int(day))
        delta = today_date - user_date
        minutes = delta.days * 24 * 60
        print(int_to_english(minutes))

    else:
        return sys.exit("Invalid date.")


def validate_date(date):
    if match := re.search(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])$", date):
        return True
    else:
        return False

def int_to_english(i):
    p = inflect.engine()
    words = p.number_to_words(i, andword="")
    return words.capitalize() + " minutes"

...


if __name__ == "__main__":
    main()