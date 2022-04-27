from flask import Flask, send_from_directory
from main.views import main
from loader.views import loader
import logging

UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(loader)

app.config['SECRET_KEY'] = 'the best key'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('log.log', encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s : %(message)s'))
logger.addHandler(file_handler)


@app.route("/uploads/images/<path:path>")
def static_dir(path):
    """Отдача загруженных файлов"""
    return send_from_directory(UPLOAD_FOLDER, path)


app.run()
