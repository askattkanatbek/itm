'''def main():
    d = {'website': "google", 'url': 'google.ru' }
    try:
        data=d['url']
    except:
        data = "htpps//"
    else:
        data = data.upper()
        print(data)
main()'''

'''5-Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0. 
Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю попробовать еще раз с другими коэффициентами.
При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции.'''
'''import logging

logging.basicConfig(level=logging.INFO, filename="logs", filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("an info")
logging.warning('a warning')
logging.error('an error')
logging.critical("a message of critical severity")


def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    logging.info('Все сработало успешно!')
    return d


try:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = discriminant(a,b,c)
    print(d)

    if d > 0:
        x1 = (-b + (d ** 0.5)) / (2 * a)
        x2 = (-b - (d ** 0.5)) / (2 * a)
        logging.info(f'Найдено два корня: x1 = {x1}, x2 = {x2}')
    elif d == 0:
        x = -b / (2*a)
        logging.info(f'Найден один корень: x = {x}')
    else:
        logging.info("Уравнение не имеет  корней потому что дискриминант меньше нуля.")
        logging.info("Попробуйте еще раз с положительными  коэффициентами.")


except ValueError:
    logging.error("Введены некорректные значения для коэффициентов.")'''

''' 6-Написать программу для генерации случайных чисел в заданном диапозоне. 
Если пользователь ввел недопустимые границы диапазона (например, меньше нуля), 
программа должна вывести ошибку и попросить ввести диапазон заново. Информация об ошибках должна быть записана в лог'''


'''import random, logging

logging.basicConfig(level=logging.INFO, filename="logs", filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("an info")
logging.warning('a warning')
logging.error('an error')
logging.critical("a message of critical severity")


def main():
    a = int(input("первый диапозон: "))
    b = int(input(('второй диапозон: ')))
    random_nummber = random.randint(a, b)
    try:
        if a < 0:
            print('Введите диапозон которые больше нуля')
            logging.info('что-то пошло неккоректно')
        else:
            print(random_nummber)
            logging.info('все работает корректно')

    except:
        logging.info("Введите правильный диапозон заново")


main()'''

''' 7 Написать программу для нахождения среднего арифметического списка чисел. 
Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка), 
программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.     
 Информация об ошибках должна быть записана в лог. '''
'''import random, logging

logging.basicConfig(level=logging.INFO, filename="logs", filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("an info")
logging.warning('a warning')
logging.error('an error')
logging.critical("a message of critical severity")

def main():
    try:
        a = (input("введите список чисел через запятую: ").split(","))
        a = [int(num) for num in a]
        print(sum(a)/len(a))
        logging.info("все работает отлично")
    except ValueError:
        print("Введите список чисел не строки")
        logging.info("тут была ошибка")

main()'''




