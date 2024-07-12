'''Реализуйте программу калькулятор.
На вход подается три значения:
первое число, второе число и операция( *, /, + или -) .
На выходе должны получить число, после выполнения операции.'''
first_number, second_number, operation = input(': ').split()
first_number,second_number = int(first_number), int(second_number)

match operation:
    case '+':
        print(first_number+second_number)
    case '-':
        print(first_number - second_number)
    case '*':
        print(first_number*second_number)
    case "/":
        print(first_number/second_number)