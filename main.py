
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import pickle 

app = FastAPI ()
pickle_model = open ( 'classifier.pkl', 'rb' )
model = pickle.load ( pickle_model )

@app.get ( '/' )
def index ():
    return 'Welcome, this is the first page.'

@app.get ( '/{name}' )
def get_name ( name : str ):
    return { 'Welcome {} this is my website'.format(name) }

@app.post ('/predict')
def predict_banknote ( data : BankNote ):
    data = data.dict ()
    variance = data ['variance']
    skewness = data ["skewness"]
    curtosis = data ["curtosis"]
    entropy = data ["entropy"]
    prediction = model.predict ( [[variance, skewness, curtosis, entropy]] )
    if prediction[0] > 0.5:
        prediction = 'It is a False note'
    else :
        prediction = 'It is a Bank note'
    return {'Prediction du model' : prediction } 



if __name__ == '__main__':
    uvicorn.run (app, host = '127.0.0.1', port = 8000)

