# Напишите программу, которая принмает на вход число N и выдает набор произведений чисел 
# от 1 до N
# N =4
# [ 1,2,6,24]  (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input('Введите число: '))
result = 1
for i in range(1,n+1):
    result = result * i
    print(result, end=' ')


