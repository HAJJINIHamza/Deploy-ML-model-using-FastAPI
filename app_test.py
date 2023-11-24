import uvicorn
from fastapi import FastAPI


#Create application
app = FastAPI ()


#Home page
@app.get ('/')
def index (  ):
    return { 'Message : THIS IS THE HOME PAGE' }

#Other page to test the app
@app.get ( '/Welcome' )
def get_name (name : str):
    return { 'Welcome to my website': f'{name}' }

#Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run ( app, host = '127.0.0.1', port = 8000 )




