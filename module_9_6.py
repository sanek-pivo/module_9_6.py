def all_variants(text): # функция-генератор all_variants(text)
    mod = len(text) # принимает строку
    for i in range(1, mod + 1): # Функция range() возвращает последовательность
        for rans in range(mod - i + 1):
            yield text[rans:rans + i] #возвращает объект-генератор

# по условию домашнего задания
a = all_variants("abc")
for i in a:
    print(i)