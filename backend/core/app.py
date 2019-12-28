from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask import request
import requests
import datetime
from flask import jsonify
import json
from flask import Response
from flask_cors import CORS, cross_origin
from core.DB import commn, setdb
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app, origins=['127.0.0.1:5000'])
dbpass= os.getenv("dbpass")
dbUserName=os.getenv("dbUserName")
app.debug=os.getenv("FLASK_DEBUG")
DataBase=os.getenv("DB_Container_Name")

DB_URL = "postgresql://{}:{}@{}/enrolle".format(dbUserName,dbpass,DataBase)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
db=SQLAlchemy(app)



@app.route('/')
def hello():
    return "udacity enrollment backend working :)"


@app.route('/enrollments',methods=['POST'])
@cross_origin()
def enrole():
    req=request.get_json()
    print(req["nanodegree_key"])

    ID=req["nanodegree_key"]+str(req["udacity_user_key"])
    new, nextState = getDB(ID)
    print("nextState: {}".format(nextState))
    UK=req["udacity_user_key"]
    enrolAt=datetime.datetime.now()
    nanoKey=req["nanodegree_key"]
    try:
        if(new):
            Commn = commn(ID,nanoKey,enrolAt,UK,nextState)
            db.session.add(Commn)
            db.session.commit()
            state ={"state" : "sucsess :) enroled"}
        else :
            
            Commn=db.session.query(commn).get(str(ID))
            Commn.status=nextState
            print("Commn.status ",Commn.status)
            db.session.commit()
            state ={"state" :  "sucsess :) {}".format(nextState)}
        
        return jsonify(state), 200


    except ValueError:
        state ={"state" :  "faild :( to {} please try again later".format(nextState)}
        print(ValueError)
        return jsonify(state), 400


def getDB(id):
    Commn=commn.query.get(str(id))
    exists = Commn is not None
    if (exists and Commn.status == 'enrole'): 
        return 0,'unenrole'
    elif (exists and Commn.status == 'unenrole'):
        return 0, 'enrole'    
    print(exists)
    return 1, 'enrole'


if __name__ == '__main__':
    setdb()
    app.run(host='0.0.0.0')
