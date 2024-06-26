# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen():

    print("Welcome to the PyPassword Random Password Generator!\n")
    nr_letters = int(input(f"How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Easy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    # #My Easy code starts here:
    # password = []

    # for letter in range(nr_letters):
    #   password += random.choice(letters)

    # for sym in range(nr_symbols):
    #   password += random.choice(symbols)

    # for num in range(nr_numbers):
    #   password += random.choice(numbers)

    # new_pwd = ''
    # for i in password:
    #   new_pwd += i

    # print(f'\nYour new password is: {new_pwd}')

    #  Hard Level - Order of characters randomised:
    #  e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    # # My Hard code starts here:

    password = []

    for letter in range(nr_letters):
        password += random.choice(letters)

    for sym in range(nr_symbols):
        password += random.choice(symbols)

    for num in range(nr_numbers):
        password += random.choice(numbers)

    random.shuffle(password)
    new_pwd = ''
    for i in password:
        new_pwd += i

    print(f'\nYour new password is: {new_pwd}\n')
    gen()


gen()
