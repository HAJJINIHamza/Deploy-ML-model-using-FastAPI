
import uvicorn
from fastapi import FastAPI

app = FastAPI ()

@app.get ( '/' )
def index ():
    return 'Welcome, this is the first page.'

@app.get ( '/{name}' )
def get_name ( name : str ):
    return { 'Welcome {} this is my website'.format(name) }

@app.get ( '/prediction' )


if __name__ == '__main__':
    uvicorn.run (app, host = 127.0.0.1, port = 8000)

