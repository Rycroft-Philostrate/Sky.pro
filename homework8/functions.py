from random import sample
from question import Question
import json


def create_list(dict_questions):
    """
    Cоздание списка экземпляров класса
    """
    list_class = []
    for q in dict_questions:
        list_class.append(Question(q['q'], q['d'], q['a']))
    return list_class


def load_question():
    """
    Загрузка впросов из файла
    """
    with open('questions.json') as f:
        return json.load(f)


def random_questions(list_question):
    """
    Формирование случайного порядка вопросов
    """
    return sample(list_question, len(list_question))


def statistic(list_result):
    """
    Фомирование и вывод статистики
    """
    scores = 0  # баллы
    current_answer = 0  # количество верных ответов
    for result in list_result:
        if result.is_correct():
            current_answer += 1
            scores += getattr(result, 'scores_question')
    if current_answer % 10 in [5, 6, 7, 8, 9, 0] or current_answer % 100 in [11, 12, 13, 14]:
        form_question = 'вопросов'
    elif current_answer % 10 == 1:
        form_question = 'вопрос'
    else:
        form_question = 'вопроса'
    return f'\nВот и все!\nОтвечено на {current_answer} {form_question} из {len(list_result)}.' \
           f'\nНабрано баллов: {scores}.'
