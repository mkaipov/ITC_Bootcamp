'''
Четвертое Задание 
Собеседование
Должен
знать либо python, либо java, либо javascript. Возраст от 18 до 65. Опыт
от 3х лет. Зарплата до 60000. Вывести результат, подходит кандидат или
нет.
'''
candidate_programming_language = input('Введите язык программирование с которым знакомы: ')
candidate_work_experience = input('Введите стаж работы в целых годах: ')
candidate_salary_expectation = input('Введите зарплатные ожидания: ')

wanted_programming_languages = ['python', 'java', 'javascript']

if candidate_programming_language in wanted_programming_languages and int(candidate_work_experience) >= 3 \
    and int(candidate_salary_expectation) <= 60000:
    print('Подходит')
else:
    print('Не подходит')
    