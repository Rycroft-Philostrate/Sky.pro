words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}  # словарь со словами легкого уровня сложности

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}  # словарь со словами среднего уровня сложности

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}  # словарь со словами сложного уровня сложности

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}  # словарь с уровнями которые получает пользователь после решения задач

difficulty_levels = {'легкий': words_easy, 'средний': words_medium, 'сложный': words_hard}
answers = {}  # словарь с ответами
counts_answer = 0  # количество верных ответов

print('Выберите уровень сложности.')
difficulty_level = input('Легкий, средний, сложный? ').casefold()
words = difficulty_levels[difficulty_level]  # словарь с выбранным уровнем сложности
print(f'Выбран {difficulty_level} уровень сложности, мы предложим 5 слов, подберите перевод.')

for key, value in words.items():  # перебор словаря со словами выбранного уровня сложности
    input('нажмите Enter ')
    print(f'{key}, {len(value)} букв, начинается на {value[0]}...')
    answer = input().casefold()
    if answer == value:
        print(f'Верно, {key} это "{value}".')
        answers[key] = True
        counts_answer += 1
    else:
        print(f'Неверно, {key} это "{value}".')
        answers[key] = False

print('Правильно отвечены слова:')
for key, value in answers.items():
    if value:
        print(key)
print('Неправильно отвечены слова:')
for key, value in answers.items():
    if not value:
        print(key)
print('Ваш ранг:')
print(levels[counts_answer])
