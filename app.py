import json
from flask import Flask
app = Flask(__name__)


@app.route('/count')
def count():
    #read - FIRST
    file = open('data.json', 'r')
    data = json.load(file)
    count = data["count"]

    #logic
    count = (count +1)
    data = {"count": count}

    #write
    file = open('data.json', 'w')
    json.dump(data, file)    

    #read - SECOND
    file = open('data.json', 'r')
    data = json.load(file)
    #print(data)
    return(data)