# Выбрать слова, начинающиеся со строчных букв
# Исключить цифры и символы
# Исключить повторяющиеся слова
# Записать в новый файл

# 'E:\PYTHON\GOBBO\list-of-colors.txt'

import re

with open('E:\PYTHON\GOBBO\list-of-colors.txt', 'r') as f:
    f = f.read().splitlines() # Разделяет на слова между пробелами
    for line in f: # Выбирает слова, начинающиеся только с маленькой буквы без символов и цифр
        for word in line.split(' '):
            if word.islower() and re.compile('[^a-z ]'):
              	print(word)
