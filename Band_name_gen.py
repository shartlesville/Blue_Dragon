#1. Create a greeting for your program.
print("Welcome to the Band Name Generator!\n")
#2. Ask the user for the city that they grew up in.
city = input("In what city did you grow up?:\n")
#3. Ask the user for the name of a pet.
pet = input("What is your pet's name?:\n")
#4. Combine the name of their city and pet and show them their band name.
band_name = city + " " + pet
#5. Make sure the input cursor shows on a new line:
print(f'Your new band name is {band_name}')