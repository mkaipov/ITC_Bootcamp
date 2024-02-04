'''
Выбор компьютера
Написать программу по выбору компьютера. 
Нужен компьютер от 4 до 8 GB оперативной памяти.
Размер жесткого диска как минимум 256, если SSD. Если HDD, то как минимум 1 террабайт.
Стоимость ноутбука не должна превышать 1000$.
Состояние новый
'''
ram_correct_input = False
while ram_correct_input == False:
    RAM = input('Enter RAM amount in GB: ')
    if RAM.isnumeric():
        ram_correct_input = True
    elif RAM.replace(".", "").isnumeric():
        ram_correct_input = False

hdd_correct_input = False
while hdd_correct_input == False:
    HDD = input('Enter Disk Drive size in GB: ')
    if RAM.isnumeric():
        hdd_correct_input = True
    elif HDD.replace(".", "").isnumeric():
        hdd_correct_input = False

hdd_type_correct_input = False
while hdd_type_correct_input == False:
    HDD_type = input('Enter type of Disk Drive (HDD or SSD): ')
    if HDD_type.lower() in ('hdd', 'ssd'):
        hdd_type_correct_input = True

price_correct_input = False
while price_correct_input == False:
    laptop_price = input('Enter laptop price in US Dollars: ')
    if laptop_price.isnumeric():
        price_correct_input = True

laptop_condition = input('Please enter laptop condition (brandnew, refurbushed, used)')

if laptop_price.find('.'):
    laptop_price = float(laptop_price)
else:
    laptop_price = int(laptop_price)


if 4 <= int(RAM) <= 8 and HDD_type.lower() == 'ssd' and int(HDD) >= 256 and laptop_price <= 1000 and laptop_condition.lower() == 'brandnew':
    print('Deal')
elif 4 <= int(RAM) <= 8 and HDD_type.lower() == 'hdd' and int(HDD) >= 1000 and laptop_price <= 1000 and laptop_condition.lower() == 'brandnew':
    print('Deal')
