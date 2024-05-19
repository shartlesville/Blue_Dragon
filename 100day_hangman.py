import random
import os
from hangman_words import word_list
stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    '''


def clear():
    os.system('cls')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
letters = []

for _ in chosen_word:
    letters.append(_)
for _ in range(word_length):
    display += "_"

guesses = []
chances = 6
print(logo)
while chances > 0:

    guess = input('\nChoose a letter: ').lower()
    if guess in guesses:
        print("You already picked that letter, try again.")
        chances -= 0
        clear()
    guesses.append(guess)
    for pos in range(word_length):
        char = chosen_word[pos]
        if char == guess:
            display[pos] = char
            chances -= 0
    if display == letters:
        print(f'\nWINNER! The word was: {chosen_word}')
        break
    elif guess not in chosen_word:
        chances -= 1

    print(f'\nWord to guess: {' '.join(display)}\n')
    print(f'You have chosen these letters: {guesses}')

    print(stages[chances])
    if chances == 0:
        print(f'\nSorry, you lose. The word was: {chosen_word}')
