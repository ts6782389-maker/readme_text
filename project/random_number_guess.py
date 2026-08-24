import random

secret_number = random.randint(1,100)

while True:
    guess = int(input("enter the guess from (1-100): "))

    if guess == secret_number:
        print("your guess is right")
        break
    elif guess > secret_number:
        print("guess a lesser number")
    else:
        print("guess a greater nummber")

    print(" -- game over -- ")

