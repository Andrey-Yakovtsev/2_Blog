from flask import Flask
from views.index import index_app
from views.post import posts_app
from models import db


app = Flask(__name__)
app.register_blueprint(index_app, url_prefix='/')
app.register_blueprint(posts_app, url_prefix='/posts')
app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///blog_new.db', SQLALCHEMY_TRACK_MODIFICATIONS=False)
db.init_app(app)

@app.route('/category/<category_id>')
def show_posts_by_category(category_id):
    pass


@app.route('/tag/<tag_id>')
def show_posts_by_tag(tag_id):
    pass

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=5000,
        debug=True
    )