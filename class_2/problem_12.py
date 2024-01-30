import datetime

user_year = int(input())
current_year = datetime.date.today().year

if user_year < current_year:
    print('Год прошел')
elif user_year > current_year:
    print('Год еще не наступил')
else:
    print('Текущий год')
