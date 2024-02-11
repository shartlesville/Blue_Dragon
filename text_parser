print('Welcome to the Text Parser')
print()

text = input('Enter your text: ')
text = text.lower() # To account for upper and lower letters
text2 = text # To be able to get the letter counts
letter1 = input('Choose a random letter: ')
letter1 = letter1.lower()
letter2 = input('Choose a 2nd random letter: ')
letter2 = letter2.lower()
letter3 = input('Choose a 3rd random letter: ')
letter3 = letter3.lower()

print()#readability

print('How many times do your random letters appear in your text?')
text2 = list(text2) #counting the letters
print("Letter", letter1, "= ", text2.count(letter1), '\n'"Letter", letter2, "= ", text2.count(letter2), '\n'"Letter", letter3, '= ', text2.count(letter3))

print()
text = list(text.split()) # To get a word count
text_length = len(text)
print("Total number of words in your text = ",text_length)
print()

first = text2[0] #indexing the first and last word
last = text2[-1]
print(f"The first letter in your text is '{first}' and the last letter in your text is '{last}'")
print()

print("If you reversed your text is would read: ") #reversing the text
print('"', end="")
print(" ".join(text[::-1]), end="")
print('"')

print()
print('"Python" is in the text, True or False = ', ("python" in text))
