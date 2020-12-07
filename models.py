from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///blog.db')
Base = declarative_base(bind=engine)
metadata = MetaData(bind=engine)


posts_tags_m2m_table = Table(
    'posts_tags',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    text = Column(Text, nullable=False)
    is_published = Column(Boolean, nullable=False, default=False, server_default='0')
    tags = relationship('Tag', secondary=posts_tags_m2m_table, back_populates='posts')
    category_id = Column(Integer, ForeignKey('Category.id'), nullable=False)


class Category(Base):
    __tablename__ ='categories'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), nullable=False)
    posts = relationship(Post, back_populates='categories')


class Tag(Base):
    __tablename__ ='tags'

    id = Column(Integer, primary_key=True, nullable=False)
    tag_title = Column(String(50), nullable=False, unique=True)
    posts = relationship(Post, secondary=posts_tags_m2m_table, back_populates='tags')

if __name__ == '__main__':
    #DB create
    Base.metadata.create_all()
