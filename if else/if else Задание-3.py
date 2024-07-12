# Даны два числа. Вывести вначале большее, а затем меньшее из них.
first_number = int(input(': '))
second_number = int(input(": "))
if first_number>second_number:
    print(first_number)
    print(second_number)
elif second_number>first_number:
    print(second_number)
    print(first_number)

