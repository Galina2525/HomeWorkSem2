#Задайте список из N элементов, заполненных числами из промежутка [-N,N]
# найдите произведение элементов на указанных индексах. Индексы вводятся
# одной строкой через пробел.
# n = 3
#[-3,-2,-1,0, 1, 2 , 3]
# --> 0  2 3
# -3*-1*0 = 0
# вывод 0
n = int(input('Введите число: ')) #пока это только строка
my_list = list(range(-n,n+1)) # формируем список
print(my_list)

indexes = input('Введите индексы: ')
my_indexes = indexes.split(' ') # разделяем индексы пробелами
nums = list(map(int,my_indexes))# формируем еще один лист из индексов
result = 1
for i in range(len(nums)):# для индексов в списке индексов
    j = int(nums[i]) # это сами индексы в списке индексов
    print(my_list[j], end=' ') # выбираем и выводим  элементы с искомыми индексами
    result = result * my_list[j] # перемножаем найденные элементы между собой
print()
print(result)    

