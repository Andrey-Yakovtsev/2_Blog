from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_new.db'
db = SQLAlchemy(app)



posts_tags_m2m_table = db.Table(
    'posts_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)


class Category(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=True)
    posts = db.relationship('Post', backref='categories', lazy=True)

    def __str__(self):
        return str(self.title)

    def __repr__(self):
        return self.__str__()


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    picture = db.Column(db.String(250), nullable=True)
    title = db.Column(db.String(75), nullable=False)
    text = db.Column(db.Text, nullable=False)
    is_published = db.Column(db.Boolean, nullable=False, default=True, server_default='1')
    tags = db.relationship('Tag', secondary=posts_tags_m2m_table, lazy='subquery',
                           backref=db.backref('tags', lazy=True))
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id),
                            nullable=True)


    def __str__(self):
        return str(self.title)



class Tag(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False, unique=True)

    def __str__(self):
        return str(self.title)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    # DB create
    db.create_all()
