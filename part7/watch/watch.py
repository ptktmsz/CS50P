import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"src=\"(https?://(?:www\.)?youtube\.com/embed/.+?)\"", s):
        cleanurl = re.sub(r"www\.", "", matches.group(1))
        cleanurl = re.sub(r"youtube\.com", "youtu.be", cleanurl)
        cleanurl = re.sub(r"http://", "https://", cleanurl)
        cleanurl = re.sub(r"embed/", "", cleanurl)
        return cleanurl

if __name__ == "__main__":
    main()