from random import randint

name = input("Tell me your name: \n")
print(f'Hi {name}, shall we play a game?')
print()
print(f"I'm thinking of a number between 1 and 100.\nYou have 8 chances to guess it.\n")

secret_number = randint(1, 100)
guesses = 8
for i in range(1, 9):
    guess = int(input("What is your guess: "))
    if guess < 0 or guess > 100:
        print(f"Your guess needs to be between 1 and 100. Try again.")
    elif guess > secret_number:
        print(f"Too high. You have {guesses - 1} more chances.")
    elif guess < secret_number:
        print(f"Too low. You have {guesses - 1} more chances.")
    elif guess == secret_number:
        print(f"Congratulations! You win! It took you {9 - guesses} tries!")
        break
    guesses -= 1
if guesses == 0:
    print(f"Sorry, {name}, you have run out of tries. The secret number was {secret_number}. Better luck next time.")
