#pytech_delete.py
#Brendan Spurlock
#07/08/2023
#Updating a pytech document

#import statements and data required for connection
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.xoqvfke.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)

#database and collection
db = client.pytech
students = db.students

#display all docs within "students" collection
student_list = students.find({})


print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

#test doc student info to be deleted
test_doc = {
    "student_id" : "1010",
    "first_name" : "Solid",
    "last_name" : "Snake"
}

#inserts student doc
test_doc_id = students.insert_one(test_doc).inserted_id

print("\n")
print("-- INSERT STATEMENTS --")
print(" Inserted student record into the students collection with document_id " + str(test_doc_id))

#find student 1010
student_test_doc = students.find_one({"student_id" : "1010"})

#displays test doc
print("\n -- DISPLAYING STUDENT TEST DOC -- ")
print(" Student ID: " + student_test_doc["student_id"] + "\n First Name: " + student_test_doc["first_name"] + "\n Last Name: " + student_test_doc["last_name"] + "\n")

#deletes student 1010
deleted_student_test_doc = students.delete_one({"student_id" : "1010"})

#displays list, again omitting the test doc due to deletion
new_student_list = students.find({})
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in new_student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

input("End of program, press any key to continue...")