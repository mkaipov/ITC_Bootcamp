user_set = set({})
for num in range(10):
    user_set.add(input('Введите любое число: '))
user_set = frozenset(user_set)
print(type(user_set))