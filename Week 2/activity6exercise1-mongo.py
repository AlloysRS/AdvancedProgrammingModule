# Import libraries as required
import pymongo
import json
import pprint

# Connect to MongoDB and setup the database and collection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["people_db"]
collection = db["students"]

# Drop the collection if it already exists, then load data from JSON
if "students" in db.list_collection_names():
    collection.drop()

# Load data into MongoDB
with open('People.json') as file:
    data = json.load(file)
    for student in data["students"]:
        student_doc = {
            "_id": student['id'],
            "title": student['fullName']['title'],
            "first_name": student['fullName']['first'],
            "surname": student['fullName']['surname'],
            "other_names": [name for name in student['fullName']['other'] if name],
            "age": student['age'],
            "city": student['city']
        }
        collection.insert_one(student_doc)
print("Data loaded successfully into MongoDB.")

# Function to get full names of people over 25
def get_names_over_25():
    results = collection.find({"age": {"$gt": 25}}, {"_id": 0, "title": 1, "first_name": 1, "surname": 1, "other_names": 1})
    print("\nFull names of people over 25:")
    for student in results:
        other_names = ' '.join(student.get('other_names', []))
        full_name = f"{student['title']} {student['first_name']} {student['surname']}" + (f", {other_names}" if other_names else "")
        print(full_name)

# Function to get IDs of people without middle names
def get_ids_no_middle_names():
    results = collection.find({"other_names": {"$exists": True, "$size": 0}}, {"_id": 1})
    print("\nIDs of people without middle names:")
    for student in results:
        print(student["_id"])

# Function to count men and women not living in Tokyo
def count_men_women_not_in_tokyo():
    pipeline = [
        {"$match": {"city": {"$ne": "Tokyo"}}},
        {"$group": {
            "_id": {"$cond": [{"$eq": ["$title", "Mr"]}, "Men", "Women"]},
            "count": {"$sum": 1}
        }}
    ]
    results = collection.aggregate(pipeline)
    print("\nCount of men and women not living in Tokyo:")
    for result in results:
        print(f"{result['_id']}: {result['count']}")

# Menu system
def menu():
    while True:
        print("\nMenu:")
        print("1. Get full names of people over 25")
        print("2. Get IDs of people without middle names")
        print("3. Count men and women not living in Tokyo")
        print("0. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            get_names_over_25()
        elif choice == '2':
            get_ids_no_middle_names()
        elif choice == '3':
            count_men_women_not_in_tokyo()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()