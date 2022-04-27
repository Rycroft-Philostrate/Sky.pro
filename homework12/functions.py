import json


def load_file():
    """Возвращает все посты"""
    try:
        with open('posts.json', encoding='utf-8') as file:
            posts = json.load(file)
    except FileNotFoundError:
        return 'Файл posts.json отсутствует'
    except json.JSONDecodeError:
        return 'Файл posts.json не формируется в список'
    else:
        return posts


def find_posts(input_text):
    """Возврашает посты по ключевому слову"""
    posts = []
    for post in load_file():
        if input_text.lower() in post['content'].lower():
            posts.append(post)
    return posts


def upload_post(path, content):
    """Записть поста в json файл"""
    data = load_file()
    data.append({'pic': path, 'content': content})
    with open('posts.json', 'w', encoding='utf8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
