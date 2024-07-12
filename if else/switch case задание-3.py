'''Даны два целых числа: D (день) и M (месяц),
определяющие правильную дату невисокосного года.
Вывести значения D и M для даты, следующей за указанной.'''
day = int(input("day: "))
month = int(input('month: '))
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        match day:
            case 31:
                month += 1
                day = 1
            case _:
                day += 1
    case 4 | 5 | 9 | 11:
        match day:
            case 30:
                month += 1
                day = 1
            case _:
                day += 1
    case 2:
        match day:
            case 28:
                month += 1
                day = 1
            case _:
                day += 1
    case 12:
        match day:
            case 31:
                month, day = 1, 1
            case _:
                day += 1
print(day, month)
