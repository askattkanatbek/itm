'''Напишите программу для вывода таблицы умножения от 0 до 9.
Используйте вложенный цикл for,
print и rangeПример:
0*1 = 00 *2 = 0…..9*1 = 99*2=18'''
for i in range(0, 10):
    for b in range(1,10):
        print(i,'*',b,"=",i*b)
