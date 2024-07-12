#Даны три целых числа. Найти количество положительных чисел в исходном наборе.
lst = []
first_nimber = int(input(": "))
second_number = int(input(': '))
third_number = int(input(': '))
if first_nimber>0:
    lst.append(first_nimber)
if second_number>0:
    lst.append(second_number)
if third_number>0:
    lst.append(third_number)
print(lst,'количество: ',len(lst))