def return_distincts(num1, num2, num3):
    sum1 = num1 + num2 + num3
    if sum1 > 15:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else:
            return num3
    if sum1 < 10:
        if num1 < num2 and num1 < num3:
            return num1
        elif num2 < num1 and num2 < num3:
            return num2
        else:
            return num3
    if 10 <= sum1 <= 15:
        if (num2 < num1 < num3) or (num2 > num1 > num3):
            return num1
        elif (num1 < num2 < num3) or (num1 > num2 > num3):
            return num2
        else:
            return num3
print(return_distincts(1, 2, 5))