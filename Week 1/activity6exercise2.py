class Name:
    def __init__(self, firstName, surname, title="No Title", otherNames=None):
        # Initialise Name instance with firstName, surname, title (optional) and list of otherNames (optional)
        self.firstName = firstName
        self.surname = surname
        self.title = title
        self.otherNames = otherNames if otherNames is not None else []

    def formalName(self):
        # Generate formal name string with initials from otherNames if exists
        initials = " ".join(f"{name[0]}." for name in self.otherNames)
        if initials:
            return f"{self.title} {self.firstName[0]}. {initials} {self.surname}"
        else:
            return f"{self.title} {self.firstName[0]}. {self.surname}"

class Person:
    def __init__(self, name: Name):
        # Initialise Person instance with a Name object
        self.name = name

class Student(Person):
    def __init__(self, name: Name):
        # Initialise Student instance as a subclass of Person, calling parent class Person's constructor with name argument
        super().__init__(name)

class DistanceStudent(Student):
    def __init__(self, name: Name, currentModule):
        # Initialise DistanceStudent instance as a subclass of Student, calling parent class Student's constructor with name argument and additional currentModule attribute
        super().__init__(name)
        self.currentModule = currentModule

    def studyInfo(self):
        # Return formatted string about current module
        return f"{self.name.formalName()} is currently studying the {self.currentModule} module."
    
# Create a Name instance with title, first name, surname, and middle names
name = Name(firstName="John", surname="Greenhold", title="Mr", otherNames=["Samuel"])

# Create a DistanceStudent instance
distance_student = DistanceStudent(name=name, currentModule="Advanced Programming")

# Print out the study information
print(distance_student.studyInfo())