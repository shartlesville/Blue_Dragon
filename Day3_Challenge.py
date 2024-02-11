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

text2 = list(text2) #counting the letters
print("Letter", letter1, "= ", text2.count(letter1), '\n'"Letter", letter2, "= ", text2.count(letter2), '\n'"Letter", letter3, '= ', text2.count(letter3))

text = list(text.split()) # To get a word count
text_length = len(text)
print("Total number of words:", text_length)
print()

first = text[0] #indexing the first and last word
last = text[-1]
print("First word:", first +'\n'"Last word: " + last)
print()

print("Reversed text: ", end='') #reversing the text
print(" ".join(text[::-1]))
print()


print('"Python" is in the text, True or False = ', ("python" in text))
