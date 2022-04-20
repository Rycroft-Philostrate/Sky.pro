from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route('/')
def list_candidates():
	"""Вывод списка всех кандидатов"""
	return render_template('list.html', data=load_candidates_from_json())


@app.route('/candidate/<name>')
def candidate_single(name):
	"""Вывод информации про кандидата по имени"""
	for candidate in load_candidates_from_json():
		if candidate['name'] == name:
			return render_template('single.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_candidate_name(candidate_name):
	"""Вывод списка кандидатов по имени"""
	result_search = get_candidates_by_name(candidate_name)
	return render_template('search.html', result_search=result_search, count_candidate_search=len(result_search))


@app.route('/skill/<skill_name>')
def search_candidate_skill(skill_name):
	"""Вывод списка кандидатов по навыку"""
	result_search = get_candidates_by_skill(skill_name)
	return render_template('skill.html', result_search=result_search, skill_name=skill_name)


if __name__ == '__main__':
	app.run()
