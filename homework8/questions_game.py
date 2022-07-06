from functions import *


questions = random_questions(create_list(load_question()))  # случайный список вопросов
print('Игра начинается!')
for question in questions:
    setattr(question, 'status_question', True)
    print(question.build_question())
    setattr(question, 'answer_user', input('Введите ответ: ').lower())
    print(question.build_feedback())
print(statistic(questions))
