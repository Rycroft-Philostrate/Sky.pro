import json


def load_questions():
	"""
	Загрузка вопросов
	"""
	with open('questions.json', encoding='utf-8') as file:
		questions = json.load(file)
	return questions


def show_field(questions):
	"""
	Построение поля
	"""
	field = ''
	for key, value in questions.items():
		field += f'{key.ljust(len(max(questions.keys(), key=len)) + 3)}'
		for k, v in value.items():
			if not v['asked']:
				field += f'{k.ljust(5)}'
			else:
				field += f'{"".ljust(5)}'
		if key != list(questions.keys())[-1]:
			field += '\n'
	return field


def parse_input(data):
	"""
	Парсер ввода пользователя
	"""
	return data.split()


def show_question(questions, data):
	"""
	Вывод вопросов
	"""
	if len(data) != 2 or data[0].capitalize() not in questions.keys() or data[1] not in questions[
		data[0].capitalize()].keys() or questions[data[0].capitalize()][data[1]]["asked"]:
		return False
	else:
		return f'Слово {questions[data[0].capitalize()][data[1]]["question"]} в переводе означает ...'


def correct_answer(questions, data):
	"""
	Правильный ответ на вопрос
	"""
	return questions[data[0].capitalize()][data[1]]['answer']


def question_used(questions, data):
	"""
	Переключение asked
	"""
	questions[data[0].capitalize()][data[1]]['asked'] = True


def save_results_to_file(scores, correct, incorrect):
	"""
	Сохранение результата в JSON файл
	"""
	result = {'points': scores, 'correct': correct, 'incorrect': incorrect}
	with open('result.json', 'w', encoding='utf-8') as file:
		json.dump(result, file, indent=2)


def check_questions(questions):
	"""
	Проверка есть ли еще вопросы
	"""
	for value in questions.values():
		for v in value.values():
			if not v['asked']:
				return True
	return False


questions_load = load_questions()
print('Начнем игру!')
scores_user = 0  # баллы пользователя
correct_answers = 0  # количество правильных ответов
incorrect_answer = 0  # количество неправильных ответов

while check_questions(questions_load):
	print(show_field(questions_load))
	input_question = parse_input(input('Выбирайте категорию вопроса и ставку '))
	correct_question = show_question(questions_load, input_question)
	while not correct_question:
		print('Такого вопроса нет, попробуйте еще раз!')
		input_question = parse_input(input('Выбирайте категорию вопроса и ставку '))
		correct_question = show_question(questions_load, input_question)
	print(correct_question)
	answer_correct = correct_answer(questions_load, input_question)
	if input().casefold() == answer_correct:
		scores_user += int(input_question[1])
		correct_answers += 1
		print(f'Верно, +{input_question[1]} очков! Ваш счет = {scores_user}.')
	else:
		scores_user -= int(input_question[1])
		incorrect_answer += 1
		print(f'Неверно, на самом деле ответ – {answer_correct}. –{input_question[1]} баллов. Ваш счет = {scores_user}')
	question_used(questions_load, input_question)

save_results_to_file(scores_user, correct_answers, incorrect_answer)
print('У нас закончились вопросы!')
print()
print(f'Ваш счет: {scores_user}', f'Верных ответов: {correct_answers}', sep='\n')
print(f'Неверных ответов: {incorrect_answer}')
