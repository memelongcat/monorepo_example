from fastapi import FastAPI

app = FastAPI(docs_url='/')


@app.get('/42')
def get_42():
    return 42

