#mongodb_test.py
#Brendan Spurlock
#July 2, 2023
#Test for connection to MongoDB cluster


from pymongo import MongoClient

#Connection string provided by MongoDB
url = "mongodb+srv://admin:admin@cluster0.xoqvfke.mongodb.net/pytech?retryWrites=true&w=majority" 

#For connection to MongoDB
client = MongoClient(url)

#Access to pytech database
db = client.pytech

#Print the list of collections in the pytech database
print("-- Pytech Collection List --")
print(db.list_collection_names())


input("Press any key to exit the program: ")