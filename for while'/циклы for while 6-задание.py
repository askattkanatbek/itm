'''Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран.
(Сделайте тоже самое со словарем и выведите ключ и значение)'''
a = [1, 2, 'asa', 45, 43.7, 'sd', 'askat', 'ss', 4]
for i in a:
    print(i,)

c = {'age' : 18,
     'height': 175,
     'name': 'Askat',
     'surname': "Shamshidinov",
     'car': 'BMW',
     'weight': 62}
d = c.items()
for key, value  in d:
    print(key,':'
          , value, )


