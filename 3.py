def number_to_words(num):
    list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    list_11 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    list_21 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    if num//10 == 0:
        print(list_1[num-1])
    elif num//10 == 1:
        print(list_11[num%10])
    elif num%10 == 0:
        print(list_21[num//10-2])
    else:
        print(list_21[num//10-2], list_1[num-1])

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))