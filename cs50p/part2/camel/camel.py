def main():

    camel = input("camelCase: ")
    print("snake_case: ", snakelize(camel))

def snakelize(s):
    s2 = ""
    for letter in s:
        if letter.islower():
            s2 += letter
        elif letter.isupper():
            s2 += "_" + letter.lower()
    return s2

main()