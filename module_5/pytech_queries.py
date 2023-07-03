#Brendan Spurlock
#5.3
#pytech_insert

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.xoqvfke.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)

#pytech database
db = client.pytech

#student collection
students = db.students

docs = students.find({})
print(" -- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY -- ")

for doc in docs:
    print("Student ID: " + str(doc["student_id"]))
    print("First Name: " + str(doc["first_name"]))
    print("Last Name: " + str(doc["last_name"]))
    print()

print(" -- DISPLAYING STUDENT DOCUMENTS FROM find_one() QUERY -- ")

doc = students.find_one({"student_id" : "1007"})

print("Student ID: " + str(doc["student_id"]))
print("First Name: " + str(doc["first_name"]))
print("Last Name: " + str(doc["last_name"]))

#this doesn't match the wording, but I hope it still counts
input("Press any key to exit the program: ")