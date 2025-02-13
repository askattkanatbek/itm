'''Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа,
 например: 256 — «двести пятьдесят шесть», 814 — «восемьсот четырнадцать».'''

num = int(input(': '))

units = {0:'ноль',
         1:'один',
         2:'два',
         3:'три',
         4:'четыре',
         5:'пять',
         6:'шесть',
         7:'семь',
         8:'восемь',
         9:'девять'}

ten = {2:'двадцать',
       3:'тридцать',
       4:'сорок',
       5:'пятьдесят',
       6:'шестьдесят',
       7:'семьдесят',
       8:'восемьдемят',
       9:'девяносто'}

hundreds = {1:'сто',
            2:'двести',
            3:'триста',
            4:'четыреста',
            5:'пятьсот',
            6:'шестьсот',
            7:'семьсот',
            8:'восемьсот',
            9:'девятсот'}

desyat = {10:'десять',
          11:'одиннадцать',
          12:'двенадцать',
          13:'тринадцать',
          14:'четырнадцать',
          15:'пятнадцать',
          16:'шестьнадцать',
          17:'семнадцать',
          18:'восемнадцать',
          19:'девятнадцать'}

h, t, tt, u = num // 100, num //10%10, num%100, num%10

result = hundreds[h]

match t:
    case 1:
        result+=" "+desyat[tt]
    case _ :
        if t>0:
            result += ' '+ ten[t]
        if u>0:
            result += ' '+ units[u]

print(result)

