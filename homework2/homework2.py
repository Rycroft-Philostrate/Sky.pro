questions = ['My name ___  Vova ', 'I ___ a coder ', 'I live ___ Moscow ']  # список вопросов
answers = ['is', 'am', 'in']  # список ответов
count_question = 0  # счетчик верных ответов
scores = 0  # баллов заработано

if input('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать! ') == 'ready':
    name = input('Расскажи, как тебя зовут! ')
    print(f'Привет, {name}, начинаем тренировку!')

    for i in range(len(questions)):  # перебор по индексу вопросов и ответов
        for j in range(2, -1, -1):  # перебор количества попыток
            if input(questions[i]) == answers[i]:
                count_question += 1
                scores += j + 1
                pr_scores = 'балл' if j + 1 == 1 else 'балла'  # правильность вывода слова 'балл'
                print(f'Ответ верный! Вы получаете {j + 1} {pr_scores}!')
                break
            elif j > 0:
                print(f'Неправильно. Осталось попыток: {j}, попробуйте еще раз!')
            else:
                print(f'Увы, но нет. Правильный ответ: {answers[i]}')

    question = 'вопрос' if count_question == 1 else 'вопросов' if count_question == 0 else 'вопроса'  # правильность вывода слова 'вопрос'

    print(f'Вот и все, {name}!', f'Вы ответили на {count_question} {question} из {len(questions)} верно.', sep='\n')
    print(f'Вы заработали {scores} баллов из {len(questions) * 3} возможных.')
else:
    print('Кажется, вы не хотите играть. Очень жаль.')
