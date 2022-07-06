class Question:
    """
    Класс обработки вопросов и ответов
    """
    def __init__(self, text_question, level_question, correct_question, status_question=False, answer_user=None):
        """
        Инициализация класса
        :param text_question: вопрос
        :param level_question: уровень сложности
        :param correct_question: верный ответ
        :param status_question: был ли задан вопрос
        :param answer_user: ответ пользователя
        """
        self.text_question = text_question
        self.level_question = level_question
        self.correct_question = correct_question
        self.status_question = status_question
        self.answer_user = answer_user
        self.scores_question = self.get_points()  # баллы за правильный ответ

    def __repr__(self):
        return f'Вопрос "{self.text_question}"'

    def get_points(self):
        """
        Подсчет очков исходя из уровня сложности
        """
        return int(self.level_question[0]) * 10

    def is_correct(self):
        """
        Правильный ответ или нет
        """
        return self.answer_user == self.correct_question

    def build_question(self):
        """
        Вывод вопроса и уровня сложности
        """
        return f'\nВопрос: {self.text_question}\nСложность: {self.level_question}/5'

    def build_feedback(self):
        """
        Вывод исходя из правильности ответа
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.get_points()} баллов.'
        else:
            return f'Ответ неверный, верный ответ {self.correct_question}.'
