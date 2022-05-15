def main():

    #prosi użytkownika o wprowadzenie tekstu:
    tekst = input("Wprowadź tekst do zamiany: ")

    #konwertuje tekst, używając funkcji convert, i wyświetla wynik:
    print(convert(tekst))

def convert(parametr1):
    parametr1 = parametr1.replace(":)","🙂")
    parametr1 = parametr1.replace(":(","🙁")
    return parametr1

main()