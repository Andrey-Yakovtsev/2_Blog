from flask import Flask
from views.index import index_app


app = Flask(__name__)
app.register_blueprint(index_app, url_prefix='/')


@app.route('/category/<category_id>')
def show_posts_by_category(category_id):
    pass

@app.route('/post/<post_id>')
def show_post(post_id):
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