import random
magic_number = random.randrange(1, 10, 1)
guess = int(input("Guess a number between 1 and 10\n"))
i = False
while i == False:
    if guess == magic_number:
        print("Correct!!!")
        i = True
    elif guess > 10 or guess < 1:
        guess = int(input("You are out of range. Guess again!\n"))
    elif guess != magic_number:
        guess = int(input("Oh so close! Guess again!\n"))