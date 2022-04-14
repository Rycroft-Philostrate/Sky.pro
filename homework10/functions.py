import json


def load_data():
	"""Загрузка списка кандидатов из файла"""
	with open('candidates.json', encoding='utf8') as file:
		return json.load(file)


def find_candidate_name(name):
	"""Поиск кандидата по имени"""
	for candidate in load_data():
		if name.title() == candidate['name']:
			return candidate


def find_candidates_skill(skill):
	"""Поиск кандидатов по навыкам"""
	list_candidates = []  # список кандидатов
	for item in load_data():
		if skill.lower() in item['skills'].lower().split(', '):
			list_candidates.append(item)
	return list_candidates
