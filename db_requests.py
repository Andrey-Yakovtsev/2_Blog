from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session

from models import Post, Category, Tag

engine = create_engine('sqlite:///blog.db')
Base = declarative_base(bind=engine)
metadata = MetaData(bind=engine)


def create_items_in_db():
    session = Session()
    post = Post(title="Первый пост", text='This is a post text', category_id=1, is_published=True)
    tag1 = Tag(tag_title='Здоровье')
    tag2 = Tag(tag_title='Спорт')
    tag3 = Tag(tag_title='Красота')
    # category1 = Category(title="Зожные статьи")
    # category2 = Category(title="Качковые статьи")
    session.add(post)
    # session.add(category1)
    # session.add(category2)
    session.add(tag1)
    session.add(tag2)
    session.add(tag3)
    session.flush()
    post.tags.extend((tag1, tag2))
    # post.category_id = category1.id

    session.commit()


if __name__ == '__main__':
    create_items_in_db()