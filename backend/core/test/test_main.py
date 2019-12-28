#!flask/bin/python
import os
import unittest

# from config import basedir
import core.app as APP
from sqlalchemy_utils import database_exists, create_database, drop_database
from dotenv import load_dotenv
load_dotenv()


class TestCase(unittest.TestCase):
    def setUp(self):
        print("setUp....")
        APP.app.config['TESTING'] = True
        APP.app.config['WTF_CSRF_ENABLED'] = False
        self.dbpass= os.getenv("dbpass")
        self.dbUserName=os.getenv("dbUserName")
        self.debug=os.getenv("FLASK_DEBUG")
        self.DataBase=os.getenv("DB_Container_Name")
        self.FLASK_APP=os.getenv("FLASK_APP")
        self.DB_URL = APP.DB_URL
        self.app = APP.app.test_client()

    def tearDown(self):
        print("tearDown....")
        print("-------------------")

    def test_env(self):
        print("  test_env")
        assert self.dbpass=="kid"
        assert self.dbUserName=="postgres"
        assert self.debug=="1"
        assert self.DataBase=="db"
        assert self.DB_URL == "postgresql://{}:{}@{}/enrolle".format(self.dbUserName,self.dbpass,self.DataBase) 
        assert self.FLASK_APP=="core.app"
    
    def test_index(self):
        print("  test_index")
        resp = self.app.get("/")
        assert '200 OK' == resp.status
        assert "udacity enrollment backend working :)" in str(resp.data)

    def test_cors(self):
        print("  test_cors  ")       
        resp = self.app.get("/")
        assert "Access-Control-Allow-Origin" in str(resp.headers)

    def test_db(self):
        print("  test_db")       
        assert True == database_exists(self.DB_URL)  