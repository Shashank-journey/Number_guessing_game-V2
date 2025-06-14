import random

Number_To_guess = random.randint(1, 100)
guess = None
attempts = 0

print("Welcome player, please guess a number between 1 and 100")

while guess != Number_To_guess:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < Number_To_guess:
        print("Too low!")
    elif guess > Number_To_guess:
        print("Too high!")
    else:
        print(f"Gotcha! You got it right in {attempts} attempts.")
