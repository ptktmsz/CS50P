import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.findall(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        if all(int(match) >= 0 and int(match) <=255 for match in matches[0]):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()