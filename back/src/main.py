from fastapi import FastAPI

from src.config import settings

if settings.RUN_MODE != 'prod':
    app = FastAPI(docs_url='/')
else:
    app = FastAPI()
    print('prod')

@app.get('/42')
def get_42():
    return 42

@app.get('/get_x2/{x}')
def get_x2_value(x: float):
    return 2 * x

