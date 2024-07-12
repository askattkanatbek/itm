# Робот может перемещаться в четырех направлениях («С» — север, «З» — запад, «Ю» — юг, «В» — восток)
# и принимать три цифровые команды:
# 0 — продолжать движение, 1 — поворот налево, −1 — поворот направо.
# Дан символ C — исходное направление робота и целое число N — посланная ему команда.
# Вывести направление робота после выполнения полученной команды.
C = input("исходное направление: ")
N = int(input(": "))
match N:
    case 0:
        print("в том же направлении")
    case 1:
        match C:
            case 'С':
                print('повернулось  на запад')
            case 'З':
                print('повернулось на юг ')
            case 'Ю':
                print('повернулось на восток')
            case 'В':
                print('повернулось на север')
    case -1:
        match C:
            case'С': print('повернулось  на восток')
            case'З': print('повернулось на север ')
            case'Ю': print('повернулось на запад')
            case'В': print('повернулось на юг')
