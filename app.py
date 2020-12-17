

from flask import Flask, request, render_template, redirect, flash, url_for
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from config import SQLALCHEMY_DATABASE_URI, secret_key

from views.index import index_app
from views.post import posts_app
from views.category import category_app
from models import db, User



app = Flask(__name__)
app.secret_key = secret_key
app.register_blueprint(index_app, url_prefix='/')
app.register_blueprint(posts_app, url_prefix='/posts')
app.register_blueprint(category_app, url_prefix='/categories')
app.config.update(SQLALCHEMY_TRACK_MODIFICATIONS=False)
app.config.update(SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI)
db.init_app(app)
Migrate(app, db, compare_type=True)

manager = LoginManager(app)



@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Проверьте правильность заполенния формы')
        elif password != password2:
            flash('Пароли не совпадают')
        else:
            hashed_pwd = generate_password_hash(password)
            new_user = User(login=login, password=hashed_pwd)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return render_template('index.html', user=user)
        else:
            flash('Неверный логин или пароль. '
                  'Возможно вы не зарегистрированы')
            return render_template('login.html')
    else:
        flash('Введите логин и пароль')
        return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index_app.index'))



if __name__ == '__main__':

    db.create_all()     # DB create
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )