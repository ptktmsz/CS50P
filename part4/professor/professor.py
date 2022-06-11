import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        errors = 0
        a = int(generate_integer(level))
        b = int(generate_integer(level))
        solution = a + b
        while errors < 3:
            try:
                answer = int(input(f"{a} + {b} = "))
                if answer == solution:
                    score = score +1
                    break
                else:
                    errors = errors + 1
                    print("EEE")
                    if errors == 3:
                        print(f"{a} + {b} = {solution}")
            except ValueError:
                errors = errors + 1
                print("EEE")
                if errors == 3:
                    print(f"{a} + {b} = {solution}")
    print(f"Score: {score}")

def get_level():
    # gets level of difficulty - 1, 2 or 3
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # generate a random number with level number of digits
    if level == 1:
        number = random.randint(0, 9)
    elif level == 2:
        number = random.randint(10, 99)
    elif level == 3:
        number = random.randint(100, 999)
    else:
        raise ValueError
    return int(number)

if __name__ == "__main__":
    main()