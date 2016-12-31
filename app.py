from flask import Flask, request
from peewee import * 
from flask_mysqldb import MySQL
import urllib

dbURL = "empa-1.cglbr7fncraq.us-west-2.rds.amazonaws.com:3306"
app = Flask(__name__)
mysql = MySQL(app)

@app.route("/")
def main():
	return "hello world!"

if __name__ == "__main__":
	app.run()