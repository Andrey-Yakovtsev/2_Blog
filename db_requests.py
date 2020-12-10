from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from models import Post, Category, Tag

engine = create_engine('sqlite:///blog.db')
Base = declarative_base(bind=engine)
metadata = MetaData(bind=engine)


def create_items_in_db():
    session = Session()
    post = Post(title="Первый пост", text='This is a post text', is_published=True)
    tag1 = Tag(title='Здоровье')
    tag2 = Tag(title='Спорт')
    tag3 = Tag(title='Красота')
    category1 = Category(title="Зожные статьи")
    category2 = Category(title="Качковые статьи")
    session.add(post)
    session.add(category1)
    session.add(category2)
    session.add(tag1)
    session.add(tag2)
    session.add(tag3)
    session.flush()
    post.tags.extend((tag1, tag2))
    post.category = category1.id

    session.commit()
    session.close()

def show_post_tags():
    for post in session.query(Post):
        return (f'У поста {post.title}, тэги: {post.tags}, Категория: {post.category}')


def show_posts_by_tags(tag_name):
    for post in session.query(Post).filter_by(title='Первый пост'):
        for tag in post.tags:
            if tag_name == str(tag.title):
                return post.title
            else:
                return 'No such tag'


if __name__ == '__main__':
    # create_items_in_db()
    session = Session()
    print(show_post_tags())
    print(show_posts_by_tags('Здоровье'))
    session.close()