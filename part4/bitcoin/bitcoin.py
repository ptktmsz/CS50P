import requests
import json
import sys

def main():
    try:
        print(f"${float(sys.argv[1]) * get_rate():,.4f}")
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

def get_rate():
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    return r["bpi"]["USD"]["rate_float"]

main()