# Import libraries as required
import xml.etree.ElementTree as ET
import json

# Load and parse the XML file
tree = ET.parse('People.xml')
root = tree.getroot()

# Initialise empty list for students data, this will have a dictionary for each student inside
students_list = []

# For loop to gather student data dictionaries to insert into students_list list
for student in root.findall('student'):
    # Initialise empty dictionary for student_data per student
    student_data = {}
    
    # Process first/last name and title
    fullName = student.find('fullName')
    student_data['title'] = fullName.get('title')
    student_data['firstName'] = fullName.find('firstName').text
    student_data['surname'] = fullName.find('surname').text
    
    # Process other names if they exist
    others = fullName.find('other')
    if others is not None:
        # Initialise an empty list to store other names
        name_list = []

        # Loop through each 'name' element inside 'other' and add each name to the list
        for name in others.findall('name'):
            name_list.append(name.text)

        # Assign the list to of names and the number attirbute to the 'other' key
        student_data['other'] = {
            'num': others.get('num'),
            'names': name_list
        }
    
    # Process age and city
    student_data['age'] = int(student.find('age').text)
    student_data['city'] = student.find('city').text
    
    # Append current student's data dictionary to students_list
    students_list.append(student_data)

# Create the final top level JSON structure with "students" as the top-level key
students_json = {"students": students_list}

# Write JSON data to a file with pretty formatting
with open('People.json', 'w') as json_file:
    json.dump(students_json, json_file, indent=4)

# Print JSON data to verify
print(json.dumps(students_json, indent=4))
