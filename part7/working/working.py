import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(\d{1,2})(:(\d{2}))? ([AP]M) to (\d{1,2})(:(\d{2}))? ([AP]M)", s):
        if matches.group(4) == "AM":
            if int(matches.group(1)) == 12:
                starthour = 0
            elif 0 < int(matches.group(1)) < 12:
                starthour = int(matches.group(1))
            else:
                raise ValueError
        elif matches.group(4) == "PM":
            if int(matches.group(1)) == 12:
                starthour = 12
            elif 0 < int(matches.group(1)) < 12:
                starthour = int(matches.group(1)) + 12
            else:
                raise ValueError
        if matches.group(2):
            if 0 <= int(matches.group(3)) < 60:
                startminutes = int(matches.group(3))
            else:
                raise ValueError
        else:
            startminutes = 0
        if matches.group(8) == "AM":
            if int(matches.group(5)) == 12:
                endhour = 0
            elif 0 < int(matches.group(5)) < 12:
                endhour = int(matches.group(5))
            else:
                raise ValueError
        elif matches.group(8) == "PM":
            if int(matches.group(5)) == 12:
                endhour = 12
            elif 0 < int(matches.group(5)) < 12:
                endhour = int(matches.group(5)) + 12
            else:
                raise ValueError
        if matches.group(6):
            if 0 <= int(matches.group(7)) < 60:
                endminutes = int(matches.group(7))
            else:
                raise ValueError
        else:
            endminutes = 0
        return f"{starthour:02}:{startminutes:02} to {endhour:02}:{endminutes:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()