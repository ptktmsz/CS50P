def main():
    getfraction()


def getfraction():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            if int(x) > int(y):
                pass
            elif int(x) / int(y) <= 0.01:
                print("E")
                break
            elif int(x) / int(y) >= 0.99:
                print("F")
                break
            else:
                print(int(int(x) / int(y) * 100), "%", sep="")
                break
        except (ValueError, ZeroDivisionError):
            pass


main()