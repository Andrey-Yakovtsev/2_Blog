from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Post, Category, Tag


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_new.db'
db = SQLAlchemy(app)


def create_items_in_db():
    # session = db.Session()

    post1 = Post(title="Пост про бег",
                 text='Бег - это. Бег, бег, бег, Бег, бег, бег, Бег, бег, бег, Бег, бег, бег, Бег,'
                                            ' бег, бег, Бег, бег, бег, Бег, бег, бег, Бег, бег, бег, Бег, бег, бег, Бег'
                                            ', бег, бег,  ',
                 is_published=True,
                 category_id=1)
    post2 = Post(title="Пост про штангу",
                 text='Пост про штангуПост про штангуПост про штангуПост про штангуПост про штангуПост про штангуПост про штангу'
                      'Пост про штангуПост про штангуПост про штангуПост про штангуПост про штангуПост про штангуПост '
                      'Пост про штангуПост про штангуПост про штангуПост про штангупро штангуПост про штангу',
                 is_published=True,
                 category_id=2)
    post3 = Post(title="Пост про Велик",
                 text='Велик - велик!  Велик - велик! Велик - велик! Велик - велик! Велик - велик! Велик - велик! '
                      'Велик - велик! Велик - велик! Велик - велик! Велик - велик! Велик - велик! Велик - велик! '
                      'Велик - велик! Велик - велик! Велик - велик! Велик - велик! Велик - велик! Велик - велик!',
                 is_published=True,
                 category_id=3)
    tag1 = Tag(title='Здоровье')
    tag2 = Tag(title='Спорт')
    tag3 = Tag(title='Красота')
    category1 = Category(title="Беговые статьи")
    category2 = Category(title="Качковые статьи")
    category3 = Category(title="Вело статьи")
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(category1)
    db.session.add(category2)
    db.session.add(category3)
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.add(tag3)
    db.session.flush()
    post1.tags.extend((tag1, tag2))
    post2.tags.extend((tag2, tag3))
    post3.tags.extend((tag1, tag3))
    post1.category = category1.id
    post2.category = category2.id
    post3.category = category3.id

    db.session.commit()
    db.session.close()

# def show_post_tags():
#     for post in session.query(Post):
#         return (f'У поста {post.title}, тэги: {post.tags}, Категория: {post.category}')
#
#
# def show_posts_by_tags(tag_name):
#     for post in session.query(Post).filter_by(title='Первый пост'):
#         for tag in post.tags:
#             if tag_name == str(tag.title):
#                 return post.title
#             else:
#                 return 'No such tag'


if __name__ == '__main__':
    # session = db.Session()
    create_items_in_db()
    # print(show_post_tags())
    # print(show_posts_by_tags('Здоровье'))
    # session.close()