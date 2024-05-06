print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()   # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
list1 = list(name1)
list2 = list(name2)
name_list = list1 + list2

score1 = 0
t = name_list.count("t")
score1 += t
r = name_list.count("r")
score1 += r
u = name_list.count("u")
score1 += u
e = name_list.count("e")
score1 += e
# print(score1)
score2 = 0
L = name_list.count("l")
score2 += L
o = name_list.count("o")
score2 += o
v = name_list.count("v")
score2 += v
e = name_list.count("e")
score2 += e
# print(score2)

score = str(score1) + str(score2)
score = int(score)
# print(score)

if score < 10 or score > 90:
    print(f'Your score is *{score}*, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
    print(f'Your score is *{score}*, you are alright together.')
else:
    print(f'Your score is *{score}*.')
