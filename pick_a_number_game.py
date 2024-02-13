from random import randint

name = input("Tell me your name: "'\n')
print(f'Hi {name}, shall we play a game?')
print()
print(f"I'm thinking of a number between 1 and 100."'\n'"You have 8 chances to guess it. What number do you think it is?"'\n')

secret_number = randint(1,100)
guesses = 8
for guess in range(1,9):
    guess = int(input("What is your guess: "))
    if guess > secret_number:
       print(f"Too high. You have {guesses - 1} more chances.")
    elif guess < secret_number:
       print(f"Too low. You have {guesses - 1} more chances.")
    elif guess == secret_number:
       print(f"Congratulations! You win! It took you {guesses} tries!")
       break
    guesses = guesses - 1
if guesses == 0:
    print(f"Sorry, {name}, you have run out of tries. The secret number was {secret_number}. Better luck next time.")
