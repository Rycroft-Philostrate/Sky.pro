from random import sample


def read_words():
	"""
	Чтение из файла слов
	"""
	with open('words.txt', encoding='utf-8') as file:
		words = list(map(str.strip, file.readlines()))  # список слов
	return words


def write_file(name_user, scores_user):
	"""
	Запись результатов в файл
	"""
	with open('history.txt', 'a', encoding='utf-8') as file:
		file.write(f'{name_user} {scores_user}\n')


def read_result():
	"""
	Чтение статистики из файла
	"""
	with open('history.txt', encoding='utf-8') as file:
		statistic = []  # результаты игр
		for i in file.readlines():
			if i.split()[1].isdigit():
				statistic.append(int(i.split()[1]))
	return len(statistic), max(statistic)


name = input('Введите ваше имя ')
scores = 0  # баллы

for word in read_words():
	print(f'Угадайте слово: {"".join(sample(word, len(word)))}')
	if input().lower() == word:
		scores += 10
		print('Верно! Вы получаете 10 очков.')
	else:
		print(f'Неверно! Верный ответ – {word}.')

write_file(name, scores)
result = read_result()
print(f'Всего игр сыграно: {result[0]}')
print(f'Максимальный рекорд: {result[1]}')
