import sys
from PIL import Image
from PIL import ImageOps
import os.path

def main():
    checkargvs()
    overlay()

def checkargvs():
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    elif os.path.splitext(sys.argv[1])[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")
    elif os.path.splitext(sys.argv[2])[1] not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")
    elif os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
         sys.exit("Input and output have different extensions")

def overlay():
    try:
        # open input image
        im = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        shirtsize = shirt.size
        im = ImageOps.fit(im, size=shirtsize)
        im.paste(shirt, shirt)
        im.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

main()