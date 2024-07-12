#Дано целое число K. Вывести строку-описание оценки, соответствующей числу K (1 — «плохо»,
# 2 — «неудовлетворительно», 3 — «удовлетворительно»,
# 4 — «хорошо», 5 — «отлично»).
# Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».

k = int(input(': '))
match k:
    case 1:
        print("плохо")
    case 2:
        print('неудовлетворительно')
    case 3:
        print('удовлетворительно')
    case 4:
        print('хорошо')
    case 5:
        print('отлично')
    case _:
        print('такой оценки нету')