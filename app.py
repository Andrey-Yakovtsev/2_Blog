from flask import Flask
from flask_migrate import Migrate

from config import SQLALCHEMY_DATABASE_URI
from views.category import category_app
from views.index import index_app
from views.post import posts_app
from views.category import category_app
from models import db


app = Flask(__name__)
app.register_blueprint(index_app, url_prefix='/')
app.register_blueprint(posts_app, url_prefix='/posts')
app.register_blueprint(category_app, url_prefix='/categories')
app.config.update(SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI)
db.init_app(app)
Migrate(app, db, compare_type=True)

@app.route('/category/<category_id>')
def show_posts_by_category(category_id):
    pass


@app.route('/tag/<tag_id>')
def show_posts_by_tag(tag_id):
    pass

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )