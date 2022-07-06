print('Привет! Предлагаю проверить свои знания английского!')
name = input('Расскажи, как тебя зовут! ')
print(f'Привет, {name}, начинаем тренировку!')

count_question = 0  # счетчик верных ответов
scores = 0          # баллов заработано

if input('My name ___ Vova ') == 'is':
    count_question += 1
    scores += 10
    print('Ответ верный!', 'Вы получаете 10 баллов!', sep='\n')
else:
    print('Неправильно.', 'Правильный ответ: is', sep='\n')
if input('I ___ a coder ') == 'am':
    count_question += 1
    scores += 10
    print('Ответ верный!', 'Вы получаете 10 баллов!', sep='\n')
else:
    print('Неправильно.', 'Правильный ответ: am', sep='\n')
if input('I live ___ Moscow ') == 'in':
    count_question += 1
    scores += 10
    print('Ответ верный!', 'Вы получаете 10 баллов!', sep='\n')
else:
    print('Неправильно.', 'Правильный ответ: in', sep='\n')

question = 'вопрос' if count_question == 1 else 'вопросов' if count_question == 0 else 'вопроса'  # правильность вывода слова 'вопрос'

print(f'Вот и все, {name}!', f'Вы ответили на {count_question} {question} из 3 верно.', sep='\n')
print(f'Вы заработали {scores} баллов.', f'Это {int(100 / 3 * count_question)} процентов.', sep='\n')
