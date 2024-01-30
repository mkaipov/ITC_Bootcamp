int_a = 17391
int_b = 546
int_c = 934


modulo_a = int_a % 17
modulo_b = int_b % 17
modulo_c = int_c % 17

if modulo_a < modulo_b and modulo_a < modulo_c:
    print(int_a)
elif modulo_c < modulo_b and modulo_c < modulo_a:
    print(int_c)
else:
    print(int_b) 
