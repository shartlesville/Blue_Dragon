line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

X = input().upper()  # Where do you want to put the treasure?

# 🚨 Don't change the code above 👆
# Write your code below this row 👇

if X == 'A1':
    line1[0] = 'X'
elif X == 'B1':
    line1[1] = 'X'
elif X == 'C1':
    line1[2] = 'X'
elif X == 'A2':
    line2[0] = 'X'
elif X == 'B2':
    line2[1] = 'X'
elif X == 'C2':
    line2[2] = 'X'
elif X == 'A3':
    line3[0] = 'X'
elif X == 'B3':
    line3[1] = 'X'
else:
    line3[2] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
