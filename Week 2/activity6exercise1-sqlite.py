# Import libraries as required
import json
import sqlite3

# Load JSON data from file
json_file = 'People.json'
with open(json_file, 'r') as file:
    data = json.load(file)

# Establish a connection to the People.db SQLite database (create it if it doesn't exist)
db_file = 'People.db'
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    title TEXT,
    first_name TEXT,
    surname TEXT,
    other_names TEXT,
    age INTEGER,
    city TEXT
)
''')

# Insert JSON data if the table is empty
cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    for student in data['students']:
        cursor.execute('''
        INSERT INTO students (id, title, first_name, surname, other_names, age, city)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            student['id'],
            student['fullName']['title'],
            student['fullName']['first'],
            student['fullName']['surname'],
            ', '.join(filter(None, student['fullName']['other'])),
            student['age'],
            student['city']
        ))
    conn.commit()

# Function to get the full name of anyone over 25
def get_names_over_25():
    """Displays full names of people over 25."""
    cursor.execute('''
        SELECT title || ' ' || first_name || ' ' || surname || 
               CASE WHEN other_names != '' THEN ', ' || other_names ELSE '' END AS full_name
        FROM students
        WHERE age > 25
    ''')
    results = cursor.fetchall()
    print("\nFull names of people over 25:")
    for row in results:
        print(row[0])

# Function to get the id of anyone without middle names
def get_ids_no_middle_names():
    """Displays IDs of people without middle names."""
    cursor.execute('''
        SELECT id
        FROM students
        WHERE other_names IS NULL OR other_names = ''
    ''')
    results = cursor.fetchall()
    print("\nIDs of people without middle names:")
    for row in results:
        print(row[0])

# Function to count men and women not living in Tokyo
def count_men_women_not_in_tokyo():
    """Counts men and women not living in Tokyo."""
    cursor.execute('''
        SELECT 
            CASE 
                WHEN title = 'Mr' THEN 'Men'
                WHEN title IN ('Mrs', 'Miss') THEN 'Women'
            END AS gender,
            COUNT(*)
        FROM students
        WHERE city != 'Tokyo'
        GROUP BY gender
    ''')
    results = cursor.fetchall()
    print("\nCount of men and women not living in Tokyo:")
    for row in results:
        print(f"{row[0]}: {row[1]}")

# Function for custom SQL input
def run_custom_sql():
    """Runs a custom SQL query entered by the user."""
    print("\nEnter your SQL query. Type ';' on a new line to execute.")
    query_lines = []
    while True:
        line = input()
        if line.strip() == ';':
            break
        query_lines.append(line)
    
    query = " ".join(query_lines)
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        
        # Display column headers
        headers = [description[0] for description in cursor.description]
        print("\nQuery results:")
        print(" | ".join(headers))
        print("-" * (len(" | ".join(headers))))

        # Display each row
        for row in results:
            print(" | ".join(str(value) for value in row))
    except sqlite3.Error as e:
        print("An error occurred:", e)

# Menu program
def menu():
    """Displays the main menu and handles user choice."""
    while True:
        print("\nMenu:")
        print("1. Get full names of people over 25")
        print("2. Get IDs of people without middle names")
        print("3. Count men and women not living in Tokyo")
        print("4. Run custom SQL query")
        print("0. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            get_names_over_25()
        elif choice == '2':
            get_ids_no_middle_names()
        elif choice == '3':
            count_men_women_not_in_tokyo()
        elif choice == '4':
            run_custom_sql()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the menu
if __name__ == "__main__":
    try:
        menu()
    finally:
        conn.close()
