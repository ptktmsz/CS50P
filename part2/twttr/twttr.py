def main():

    text_to_convert = input("Input: ")
    print("Output:", convert(text_to_convert))

def is_vowel(letter):
    if letter.lower() in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False

def convert(s):
    s2 = ""
    for l in s:
        if is_vowel(l) == False:
            s2 += l
    return s2

main()