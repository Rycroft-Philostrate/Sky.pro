from flask import Blueprint, render_template, request, flash, redirect, current_app
from functions import upload_post, load_file
import os

loader = Blueprint('loader', __name__, template_folder='templates')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


@loader.route('/post', methods=["POST", "GET"])
def add_post():
    """Добавления поста"""
    if request.method == 'POST':
        result = load_file()
        if type(result) == list:
            content = request.form['content']
            if not content:
                flash('Введите текст к посту!')
                return redirect(request.url)
            file = request.files.get('picture')
            if file:
                if file.filename.split('.')[-1] not in ALLOWED_EXTENSIONS:
                    current_app.logger.info('Загруженный файл не картинка')
                    flash('Загруженный файл не картинка!')
                    return redirect(request.url)
                path_file = f"./uploads/images/{file.filename}"
                file.save(path_file)
                upload_post(path_file, content)
                return render_template('post_uploaded.html', path_file=path_file, content=content)
            else:
                current_app.logger.error('Ошибка при загрузки файла')
                return 'Ошибка при загрузки файла!'
        else:
            return result
    return render_template('post_form.html')
