students = {'Иванов': ['Русский', 'Английский', 'Французский'],
            'Сидоров': ['Русский', 'Китайский'],
            'Васнецов': ['Русский', 'Немецкий', 'Латынь'],
            'Крутов': ['Русский', 'Английский', 'Французский'],
            'Колесов': ['Русский', 'Английский'],
            'Капустин': ['Русский', 'Английский', 'Французский', 'Немецкий', 'Китайский', 'Японский', 'Молдавский'],
            'Бингчилин': ['Китайский']}

keys = list(students.keys())
values = list(students.values())
languages = []
scores = []
chinese = []

for i in students.values():
    for j in i:
        if j not in languages:
            languages.append(j)

for i in students.values():
    pos = values.index(i)
    for j in i:
        if j == 'Китайский':
            chinese.append(keys[pos])

for i in students.keys():
    scores.append(len(students[i]))
for i in range(len(students.keys())):
    print(keys[i], 'знает', scores[i], 'языков')

print('')
print('Всего', len(languages), 'языков -', *sorted(languages))
print('')
print('Студенты, знающие китайский:', *chinese)
