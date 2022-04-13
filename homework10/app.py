from flask import Flask
from functions import *

app = Flask(__name__)


@app.route('/')
def index():
	"""Главная страница, выводит список кандидатов"""
	list_candidate = '<pre>'  # список кандидатов
	for candidate in load_data():
		list_candidate += f'''\n	{candidate["name"]} -
	{candidate["position"]}
	{candidate["skills"]}\n'''
	list_candidate += '</pre>'
	return list_candidate


@app.route('/candidates/<name>')
def candidates(name):
	"""Выводит кандидата по имени"""
	candidate = find_candidate_name(name)
	return f'''<img src="{candidate['picture']}">
	
<pre>
	{candidate["name"]} - 
	{candidate["position"]}
	{candidate["skills"]}
</pre>'''


@app.route('/skills/<skill>')
def skills(skill):
	"""Выводит кандидатов по навыку"""
	list_candidate = '<pre>'  # список кандидатов
	for candidate in find_candidates_skill(skill):
		list_candidate += f'''\n	{candidate["name"]} -
	{candidate["position"]}
	{candidate["skills"]}\n'''
	list_candidate += '</pre>'
	return list_candidate


if __name__ == '__main__':
	app.run(debug=True)
