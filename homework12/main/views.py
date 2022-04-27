from flask import Blueprint, render_template, request, redirect, url_for, current_app
from functions import find_posts, load_file

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def main_index():
	"""Главная страница"""
	return render_template('index.html')


@main.route('/search')
def search_posts():
	"""Поиск постов по запросу"""
	result = load_file()
	if type(result) == list:
		input_text = request.args.get('s')
		if input_text == '':
			return redirect(url_for('main.main_index'))
		current_app.logger.info(f'Поиск постов по запросу "{input_text}"')
		return render_template('post_list.html', posts=find_posts(input_text), input_text=input_text)
	else:
		return result
