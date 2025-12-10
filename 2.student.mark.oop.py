class Student():
    def __init__(self, name = "", id = "", dob = ""):
        self.name = name
        self.id = id
        self.dob = dob
    
    def input(self):
        self.name = input("Student name: ")
        self.id = input("Student ID: ")
        self.dob = input("Student dob: ")
        
    def display(self):
        print(f"Student: {self.name}, id: {self.id}, dob: {self.dob}")
        
class Course():
    def __init__(self, name = "", id = ""):
        self.name = name
        self.id = id
    
    def input(self):
        self.name = input("Course name: ")
        self.id = input("Course ID: ")
        
    def display(self):
        print(f"Course {self.name}, id: {self.id}")

class Mark():
    def __init__(self):
        self.sid = ""
        self.cid = ""
        self.mark = 0
        
    def input(self):
        self.sid = input("Student id: ")
        self.cid = input("Course id: ")
        self.mark = float(input("Mark: "))
    
    def display(self):
        print(f"Result:  Student ID: {self.sid}, Course ID: {self.cid}, Mark: {self.mark}")
        
class MarkManagement():
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []
    
    def inputStudents(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            s = Student()
            s.input()
            self.students.append(s)
    
    def inputCourses(self):
        n = int(input("Enter number of courses: "))
        for i in range(n):
            c = Course()
            c.input()
            self.courses.append(c)
    
    def inputMarks(self):
        n = int(input("Enter number of marks: "))
        for i in range(n):
            m = Mark()
            m.input()
            self.marks.append(m)

    def displayStudents(self):
        for s in self.students:
            s.display()
        print("\nStudent: ")
    
    def displayCourses(self):
        for c in self.courses:
            c.display()
        print("\nCourses: ")
        
    def displayMarks(self):
        for m in self.marks:
            m.display()
        print("\nMarks: ")
        
system = MarkManagement()

system.inputStudents()
system.inputCourses()
system.inputMarks()

system.displayStudents()
system.displayCourses()
system.displayMarks()
    