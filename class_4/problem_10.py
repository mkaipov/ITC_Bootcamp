input_string = 'Lamborgini 17 4456 2020 Paris USA 11 23'
num_lst = []
str_lst = []

for word in input_string.split():
    if word.isdigit():
        num_lst.append(int(word))
    elif word.isalpha():
        str_lst.append(word)

print(num_lst)
print(str_lst)

