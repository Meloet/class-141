from logging import root
from h11 import Data
import pandas as pf
from flask import Flask, jsonify, request
from flask_cors import CORS
df=pf.read_csv('link.csv')
app=Flask(__name__)
CORS(app)
data=[{
    'name':df['name'].tolist(),
    'links':df['imdb_link'].tolist()
}]
@app.route('/getmovies')
def getmovies():
    return jsonify({
        'data':data
    })
if(__name__=='__main__'):
    app.run(debug=True)