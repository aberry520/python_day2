import random
magic_number = random.randrange(1, 10, 1)
guess = int(input("Guess a number between 1 and 10\n"))
while True:
    if guess == magic_number:
        print("Correct!!!\n")
        answer = input("Would you like to play again? y or n: ")
        if answer == "y":
            magic_number = random.randrange(1, 10, 1)
            guess = int(input("Guess a number between 1 and 10\n"))
            continue
        elif answer == "n":
            break
    elif guess > 10 or guess < 1:
        guess = int(input("You are out of range. Guess again!\n"))
    elif guess != magic_number:
        guess = int(input("Oh so close! Guess again!\n"))