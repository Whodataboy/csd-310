#Brendan Spurlock
#5.3
#pytech_insert

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xoqvfke.mongodb.net/pytech?retryWrites=true&w=majority" 
client = MongoClient(url)

#PyTech Database
db = client.pytech

#Student collection
students = db.students

Samus = {
    "first_name" : "Samus",
    "last_name" : "Aran",
    "student_id" : "1007"
}

Nathan = {
    "first_name" : "Nathan",
    "last_name" : "Drake",
    "student_id" : "1008"
}

Arthur = {
    "first_name" : "Arthur",
    "last_name" : "Morgan",
    "student_id" : "1009"
}

student1 = students.insert_one(Samus).inserted_id
student2 = students.insert_one(Nathan).inserted_id
student3 = students.insert_one(Arthur).inserted_id

print("--INSERT STATEMENTS--")
print("Inserted student record " + Samus["first_name"] + " " + Samus["last_name"] + " into the students collection with document_id" + str(student1))
print("Inserted student record " + Nathan["first_name"] + " " + Nathan["last_name"] + " into the student collection with document_id" + str(student2))
print("Inserted student record " + Arthur["first_name"] + " " + Arthur["last_name"] + " into the student collection with document_id" + str(student3))





