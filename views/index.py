from flask import Blueprint, render_template
from models import Post, Tag, Category

index_app = Blueprint('index_app', __name__)

@index_app.route('/', endpoint='index')
def posts_list():
    posts = Post.query.limit(3)
    return render_template('index.html', posts=posts)