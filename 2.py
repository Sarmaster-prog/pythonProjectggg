alph = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
direction = input('Выбери направление: \n(+) - Шифрование \n(-) - Дешифрование:\n ')
lang = int(input('Выбери язык алфавита: \n0 - Русский \n1 - Английский: \n'))
#step = int(direction + input('Веди число, шаг сдвига (со сдвигом вправо): '))
text = input('Введите текст для обработки:\n')
for j in range(26):
    for i in text:
        if i.isalpha():
            char = alph[lang][(alph[lang].index(i.upper()) + j ) % len(alph[lang])]
            print(char if i.isupper() else char.lower(), end='')
        else:
            print(i, end='')