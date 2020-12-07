from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session

from models import Post, Category, Tag

engine = create_engine('sqlite:///blog.db')
Base = declarative_base(bind=engine)
metadata = MetaData(bind=engine)

if __name__ == '__main__':
    def create_items_in_db():
        session = Session()
        post = Post() #параметры
        tag = Tag()
        category = Category()
        session.add(post)
        session.add(category)
        session.add(tag)

        session.flush()
        session.commit()



if __name__ == '__main__':
    #DB create
    # Base.metadata.create_all()
    pass
