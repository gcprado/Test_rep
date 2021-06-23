from number_functions import dif_even_odd as dpi
import random

list_range = random.randint(5,10)

numbers1 = []
for i in range(list_range):
    numbers1.append(random.randint(0,9))

numbers2 = []
for i in range(list_range):
    numbers2.append(random.randint(0,9))

print("A =", numbers1)
print("B =", numbers2)


even_odd = dpi(numbers1, numbers2)
print("C =", even_odd)
