import os

PG_USER = 'blog'
PG_PASSWORD = os.environ.get('POSTGRES_PASSWORD')

# PG_HOST = '127.0.0.1'     # Dockerbase
PG_HOST = 'localhost'
PG_PORT = '5432'
# PG_PORT = '5000'
PG_DB = 'blog_db'


SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}'
secret_key = 'sljfhbsldhfalweuigfw;ieufg;'