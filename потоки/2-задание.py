'''Откройте и прочитайте данные с файла lorum.txt, способом,
который рассматривается в видео из пункта 1.'''
with open(r"C:\Users\lapshop.kg\Desktop\lorum.txt", 'r', encoding='utf-8') as file:
    print(file.read())
