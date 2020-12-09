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
    session = Session()
    for post in session.query(Post):
        return post.tags

def show_posts_by_tags(tag):
    pass

def show_posts_by_category(category):
    pass



if __name__ == '__main__':
    # create_items_in_db()
    print(show_post_tags())