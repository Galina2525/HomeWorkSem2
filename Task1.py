#Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр
# 0,56 -> 11
# n = input('Введите число: ')
# result = 0
# for i in n:
#     if i.isdigit():
#         result += int(i)
# print(result)        

# еще проще для вещественных (извлекаются отдельные символы
# и преобразовываются в int)
# n = input('Введите число: ')
# result = 0
# for i in n:
#     result += int(i)
# print(result)   
## Более полное решение для положит и отриц веществ цифр

# num = input('Введите число: ').replace('.','').replace('-','')
# while not num.isdigit:
#     num = input('Введите число: ').replace('.','').replace('-','')

# my_sum = 0
# my_sum = sum(list(map(int,num)))
# print(my_sum)

# print()

## Для вещественных без строк
n = float(input('Введите вещественное число: '))
my_sum = 0
while not n.is_integer():
    n*=10
while n!=0:
    my_sum = my_sum + n % 10
    n //= 10    
print(my_sum)    






