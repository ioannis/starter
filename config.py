import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello-world-server-ioannis'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'hello-world-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacityadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'p@ssword1234'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'helloworldioannis'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '2fVO/Hq29Mq86u42r9/koy+UajxLmmJFqhBJK8p7ZUA3XskkzzzkHmTYaB6FVV1xo21UJWrOFtAYHs3eSOEvxQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
