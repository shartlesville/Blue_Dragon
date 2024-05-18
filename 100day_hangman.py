import random

word_list = ["aardvark", "baboon", "camel", "sanctuary", "letter", "pierce", "shine", "crowd", "useful", "entry", "discount", "descent", "triangle", "violation", "pneumonia", "tension", "equate", "extraordinary", "random", "treasure"]

def art():
    if chances == 6:
        print(''' 

                      |   
                      |  
                      | 
                      | 
                      | 
                      |_____
                         ''')
    elif chances == 5:
        print(''' 
                      ____
                      |   
                      |  
                      | 
                      | 
                      | 
                      |_____
                         ''')
    elif chances == 4:
        print(''' 
                      ____
                      |  | 
                      | 
                      | 
                      | 
                      | 
                      |_____
                         ''')
    elif chances == 3:
        print(''' 
                      ____
                      |  | 
                      |  O
                      | 
                      | 
                      | 
                      |_____
                         ''')
    elif chances == 2:
        print(''' 
                      ____
                      |  | 
                      |  O
                      | \\ /
                      |  
                      | 
                      |_____
                         ''')
    elif chances == 1:
        print(''' 
                      ____
                      |  | 
                      |  O
                      | \\ /
                      |  |
                      | 
                      |_____
                         ''')
    elif chances == 0:
        print(f'\nSorry, you lose. The word was: {chosen_word}')
        print(''' 
                  ____
                  |  | 
                  |  O
                  | \\ /
                  |  |
                  | / \\
                  |_____
                     ''')


chosen_word = random.choice(word_list)
display = []
letters = []

for _ in chosen_word:
    letters.append(_)
for _ in chosen_word:
    display += "_"

for _ in display:
    print(_, end=' ')
guesses = []
chances = 6

while chances > 0:

    guess = input('\nChoose a letter: ').lower()
    if guess in guesses:
        print("You already picked that letter, try again.")
        chances -= 0

    guesses.append(guess)
    for pos in range(len(chosen_word)):
        char = chosen_word[pos]
        if char == guess:
            display[pos] = char
            chances -= 0
    if display == letters:
        print(f'\nWINNER! The word was: {chosen_word}')
        break
    elif guess not in chosen_word:
        chances -= 1

    print(f'You already chose these letters: {guesses}\n')
    print(f'Word to guess: {display}')
    art()