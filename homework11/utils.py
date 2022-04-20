import json


def load_candidates_from_json():
	"""Загрузка списка кандидатов"""
	with open('candidates.json', encoding='utf8') as file:
		return json.load(file)


def get_candidate(candidate_id):
	"""Возвращает кандидата по id"""
	data = load_candidates_from_json()
	for element in data:
		if element['id'] == candidate_id:
			return element


def get_candidates_by_name(candidate_name):
	"""Возвращает список кандидатов по имени"""
	list_candidates = []  # список имен кандидатов
	data = load_candidates_from_json()
	for element in data:
		if candidate_name.lower() in element['name'].lower():
			list_candidates.append(element['name'])
	return list_candidates


def get_candidates_by_skill(skill_name):
	"""Возвращает список кандидатов по навыкам"""
	list_candidates = []  # список имен кандидатов
	data = load_candidates_from_json()
	for element in data:
		if skill_name.lower() in element['skills'].lower().split(', '):
			list_candidates.append(element['name'])
	return list_candidates
