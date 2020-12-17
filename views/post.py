from flask import Blueprint, render_template
from models import Post, Tag, Category

posts_app = Blueprint('posts_app', __name__)

@posts_app.route('/<post_id>', endpoint='post_detail')
def posts_item(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    # last = Post.query.order_by(id).first_or_404()
    return render_template('post-page.html',
                           post=post,
                           # last=last
                           )

