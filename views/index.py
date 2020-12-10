from flask import Blueprint, render_template

index_app = Blueprint('index_app', __name__)

@index_app.route('/')
def posts_list():
    return render_template('index.html')