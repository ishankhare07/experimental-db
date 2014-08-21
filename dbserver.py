from pymongo import *
import datetime,random

mongo_url = 'mongodb://ishan:websockets@oceanic.mongohq.com:10046/ishan'

client = MongoClient(mongo_url)
db = client.ishan
collection = db.notes
print 'Connected to database server...'

def show_note():
	for x in collection.find():
		print '\nTitle : ' + x["note"]
		print 'Content : ' + x["content"]
		print x["datetime"] + '\n'

def save_note():
	title = raw_input('Enter a note title : ')
	data = raw_input('Enter the note : ')
	note = {
		"_id" : int(random.random()*10**5),
		"note" : title,
		"content" : data,
		"datetime" : datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S")
	}
	try:
		collection.insert(note)
	except:
		print 'Error....try again...'

def delete_note():
	for x in collection.find():
		print '\nid : ' + str(x["_id"])
		print 'title : ' + x["note"] + '\n'
	tbd = raw_input('Enter the id of note to be deleted : ')
	try:
		collection.remove({"_id" : tbd})
	except:
		print 'Sorry....try again...'

while True:
	ch = raw_input('1. Show\n2. Save\n3. Delete\n4. Exit\n\n')

	if ch == '1':
		show_note()
	elif ch == '2':
		save_note()
	elif ch == '3':
		delete_note()
	elif ch == '4':
		print 'GoodBye...\nExiting now....'
		exit()
	else:
		print 'wrong choice!!!\ntry again...'
