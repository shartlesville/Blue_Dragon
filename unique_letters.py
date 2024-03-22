def unique_letters(word):
    letter_set = set()
    for letter in word:
        letter_set.add(letter)
    letter_list = list(letter_set)
    letter_list.sort()
    return letter_list


print(unique_letters('entertaining'))
