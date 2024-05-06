# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the Tip Calculator!\n")
bill = float(input("What is the total bill?\n"))
tip_percent = int(input("What percentage tip do you want to include?\n"))
tip = float(bill) * float(tip_percent / 100)
persons = int(input("How many people are splitting the bill?\n"))
per_person = (bill + tip) / persons

print(f'Each person should pay ${per_person:.2f}')
