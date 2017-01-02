import server
from peewee import *

# I have no idea what I'm doing.

class User(Model):

	class Meta:
		db = server.empaDB

class Patient(Model):
	image = CharField()
	firstName = CharField()
	lastName = CharField()

	class Meta:
		db = server.empaDB

class Session(Model):
	sessionLength = DoubleField()

	class Meta:
		db = server.empaDB

class SocialStory(Model):

	class Meta:
		db = server.empaDB
