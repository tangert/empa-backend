from flask import Flask, request
from peewee import * 
from flask_mysqldb import MySQL
import urllib

app = Flask(__name__)
mysql = MySQL(app)

@app.route("/")
def main():
	return "hello world!"

if __name__ == "__main__":
	app.run()