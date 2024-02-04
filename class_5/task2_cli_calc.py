# Выводим список доступных операций. Операции в списке нужны для проверки корректности ввода
available_operations = ('+','-','/','*','**', '//','%')
correct_input_operation = False
# В цикле проверяем корректность ввода операции.
while correct_input_operation == False:
    operation = input('Введите математическую операцию, доступные операции ' + ", ".join(available_operations) + ': ')
    if operation in available_operations:
        correct_input_operation = True


correct_input_digits = False
# В цикле проверяем корректность ввода чисел чтобы пользователь вводил именно целые числа или дробные числа (int, float)
while correct_input_digits == False:
    digit_1 = input('Введите первое число: ')
    digit_2 = input('Введите второе число: ')
    if digit_1.isnumeric() and digit_2.isnumeric():
        correct_input_digits = True
    elif digit_1.replace(".", "").isnumeric() and digit_2.replace(".", "").isnumeric():
        correct_input_digits = True

# Выясняем каким типом данных явлется введенное число и устанавливаем правильный тип для этой переменной.
if digit_1.find('.'):
    digit_1 = float(digit_1)
else:
    digit_1 = int(digit_1)
if digit_2.find('.'):
    digit_2 = float(digit_2)
else:
    digit_2 = int(digit_2)

# Математические операции.
if operation == '+':
    print(digit_1 + digit_2)
elif operation == '-':
    print(digit_1 - digit_2)
elif operation == '/':
    print(digit_1 / digit_2)
elif operation == '*':
    print(digit_1 * digit_2)
elif operation == '**':
    print(digit_1 ** digit_2)
elif operation == '//':
    print(digit_1 // digit_2)
elif operation == '%':
    print(digit_1 % digit_2)
