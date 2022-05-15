def main():
    user_time = input("What time is it? ")
    result = (convert(user_time))
    if 7 <= result <= 8:
        print("breakfast time")
    elif 12 <= result <= 13:
        print("lunch time")
    elif 18 <= result <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60

if __name__ == "__main__":
    main()