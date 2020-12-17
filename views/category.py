from flask import Blueprint, render_template
from models import Category

category_app = Blueprint('category_app', __name__)

@category_app.route('/<category_id>', endpoint='category_page')
def show_category_post(category_id):
    category = Category.query.filter_by(id=category_id)
    return render_template('category-page.html',
                           category=category,
                           )