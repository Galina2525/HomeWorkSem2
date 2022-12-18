# Реализуйте алгоритм перемешивания списка
num = input('Введите числа через пробел: ')
my_num = num.split(' ')
my_list = list(map(int,my_num))
print(my_list)
import random

# random.shuffle(my_list)

for i in range(len(my_list)):
    n = random.randint(0,len(my_list)-1)
    my_list[i], my_list[n] = my_list[n], my_list[i]# алгоритм перемешивания
    print(my_list[i], my_list[n])

print(my_list)

