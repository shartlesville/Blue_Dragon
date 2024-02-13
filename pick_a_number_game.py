from random import randint

name = input("Tell me your name: ")
print(f'Hi {name}, shall we play a game? Please enter yes or no. ') #add a y or n option
if input() == "yes":
    print(f"Great! I'm thinking of a number between 1 and 100. You have 8 tries to guess it. What number do you think it is?")
else:
    print(f"Ok, {name}, maybe next time.")


secret_number = randint(1,100)
guesses = 8
for guess in range(9):
    guess = int(input("What is your guess: "))
    if guess > secret_number:
       print(f"Too high, try again. You have {guesses - 1} more chances.")
    elif guess < secret_number:
       print(f"Too low, try again. You have {guesses - 1} more chances.")
    elif guess == secret_number:
       print(f"Congratulations! You win! It took you {guesses} tries!")
       break
    guesses = guesses - 1
