import datetime

user_year = int(input())
current_year = datetime.date.today().year
user_age = current_year - user_year

if user_age >= 18:
    print('Совершеннолетний')
elif user_age <= 4:
    print('Ребенок')
else:
    print('Несовершеннолетний')
