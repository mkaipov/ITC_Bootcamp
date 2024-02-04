num_a = 17531
num_b = 5821
counter = 0
while num_a > 0:
    num_a -= 3
    counter += 1

if counter > num_b:
    print('Количество троек в числе 17531 больше чем 5821')
else:
    print('Число 5821 больше')