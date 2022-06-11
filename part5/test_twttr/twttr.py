def main():
    text_to_convert = input("Input: ")
    print("Output:", shorten(text_to_convert))


def shorten(word):
    word_shortened = ""
    for l in word:
        if l.lower() not in ["a", "e", "i", "o", "u"]:
            word_shortened += l
    return word_shortened


if __name__ == "__main__":
    main()