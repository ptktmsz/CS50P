import random

# gets a positive integer
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# gets a random number between 1 and level
if level == 1:
    answer = 1
else:
    answer = random.randrange(1,level)

while True:

    try:

        # prompts user for a guess
        guess = int(input("Guess: "))

        # checks if guess is good
        if guess < 0:
            pass
        elif guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass