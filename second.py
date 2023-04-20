alph = {1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
        2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
        3: ['Б', 'Г', 'Ё', 'Ь', 'Я'],
        4: ['Й', 'Ы'],
        5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
        8: ['Ш', 'Э', 'Ю'],
        10: ['Ф', 'Щ', 'Ъ']}

word = input(print('Введите слово заглавными буквами: '))
score = 0
values = list(alph.values())
keys = list(alph.keys())
for i in word:
    for j in values:
        if i in j:
            pos = values.index(j)
            score += keys[pos]
print(score)
