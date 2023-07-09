#import statements and data required for connection
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.xoqvfke.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)

#database and collection
db = client.pytech
students = db.students

#display all docs within "students" collection
student_list = students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")


#updates student's name
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Nara"}})

#finds student for display
samus = students.find_one({"student_id": "1007"})
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")

#display's chosen student
print(" Student ID: " + samus["student_id"] + "\n First Name: " + samus["first_name"] + "\n Last Name: " + samus["last_name"] + "\n")

input("End of program, press any key to continue...")
