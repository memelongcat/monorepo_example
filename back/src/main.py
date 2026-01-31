
from fastapi import FastAPI

from src.config import settings

from sqlalchemy import create_engine

from sqlalchemy.orm import Session

from sqlalchemy import text

if settings.RUN_MODE != 'prod':
    app = FastAPI(docs_url='/')
else:
    app = FastAPI()
    print('prod')


@app.get('/init-db')
def init_db():
    engine = create_engine(f"mysql+pymysql://{settings.DB.MYSQL_USER}:{settings.DB.MYSQL_PASSWORD}@{settings.DB.MYSQL_ADDRESS}:{settings.DB.MYSQL_PORT}/{settings.DB.MYSQL_DATABASE}", echo=True)
    with engine.connect() as connection:
        result = connection.execute(text(
            "CREATE TABLE IF NOT EXISTS test ( \
                id INT AUTO_INCREMENT PRIMARY KEY, \
                num integer, \
                data varchar(255) \
            );" 
        ))    
        connection.execute(text('INSERT INTO test (num, data) VALUES (:num, :data)').bindparams(num=100, data='abc'))
        a = str([i for i in connection.execute(text('SELECT * FROM test')).all()])
        return a


@app.get('/add-data')
def init_db():
    engine = create_engine(f"mysql+pymysql://{settings.DB.MYSQL_USER}:{settings.DB.MYSQL_PASSWORD}@{settings.DB.MYSQL_ADDRESS}:{settings.DB.MYSQL_PORT}/{settings.DB.MYSQL_DATABASE}", echo=True)
    with engine.connect() as connection:
        connection.execute(text('INSERT INTO test (num, data) VALUES (:num, :data)').bindparams(num=100, data='abc'))
        a = str([i for i in connection.execute(text('SELECT * FROM test ORDER BY test.id')).all()])
        return a



#@app.get('/getdb')
#def get_db_creds():
#    tuple = (
#        settings.DB.MYSQL_ADDRESS,
#        settings.DB.MYSQL_USER,
#        settings.DB.MYSQL_PASSWORD,
#        settings.DB.MYSQL_DATABASE,
#        settings.DB.MYSQL_PORT,
#            )
#    return tuple

@app.get('/42')
def get_42():
    return 42

@app.get('/get_x2/{x}')
def get_x2_value(x: float):
    return 2 * x

