# Задайте список из n чисел последовательности (1 + 1/n)*n и выведите на экран
# их сумму
# n = 4
#{1:2, 2:2,5, 3:2,37, 4: 2,44} 
# сумма 9.06
n = int(input('Введите число: '))
s = 0
for i in range(1,n+1):
    result = (1 +1/i)**i
    result = round(result,2)
    s += result

    print(f'{i}:{result}',end=' ')
print()    
print('Сумма =',s)    
    

