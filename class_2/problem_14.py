num1, num2, num3 = int(input()), int(input()), int(input())

num_max = 0
num_min = 0
 
if num1 > num2 and num1 > num3:
    num_max = num1
elif num2 > num1 and num2 > num3:
    num_max = num2
elif num3 > num1 and num3 > num2:
    num_max = num3


if num1 < num2 and num1 < num3:
    num_min = num1
elif num2 < num1 and num2 < num3:
    num_min = num2
elif num3 < num1 and num3 < num2:
    num_min = num3

print(num_max)

print(num_min)
