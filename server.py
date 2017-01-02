from flask import Flask, request, jsonify, abort, make_response, redirect
from flask_mysqldb import MySQL
from flask_googlelogin import GoogleLogin
from peewee import *
from datetime import datetime
import os, config
import urllib

# App and DB initialization.
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'empaDB'
app.config['MYSQL_DATABASE_HOST'] = 'empa-1.cglbr7fncraq.us-west-2.rds.amazonaws.com:3306'
mysql = MySQL(app)

empaDB = pw.MySQLDatabase("empaDB",
								host="empa-1.cglbr7fncraq.us-west-2.rds.amazonaws.com:3306",
								port=3306,
								user="root", 
								passwd="root")
# fill in user and password

# DB functions.
def connectDB():

def disconnectDB():

# Login and logout.
def login():

def logout():

# Patient functions.
@app.route("", methods=['POST'])
def createPatient():
	# peewee statements here to query the database

@app.route("", methods=['GET'])
def getPatient():

@app.route("", methods=['PUT'])
def editPatient():

@app.route("", methods=['DELETE'])
def deletePatient():


# Session functions.
@app.route("", methods=['POST'])
def createSession():

@app.route("", methods=['GET'])
def getSession():

@app.route("", methods=['PUT'])
def editSession():

@app.route("", methods=['DELETE'])
def deletePatient();

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)