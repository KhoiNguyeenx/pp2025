import math
import numpy as np

class Student():
    def __init__(self, name = "", id = "", dob = ""):
        self.name = name
        self.id = id
        self.dob = dob
        self.gpa = 0.0
    
    def input(self):
        self.name = input("Student name: ")
        self.id = input("Student ID: ")
        self.dob = input("Student dob: ")
        
    def display(self):
        print(f"Student: {self.name}, id: {self.id}, dob: {self.dob}, GPA: {self.gpa}")
        
class Course():
    def __init__(self, name = "", id = "", credit = 0):
        self.name = name
        self.id = id
        self.credit = credit
    
    def input(self):
        self.name = input("Course name: ")
        self.id = input("Course ID: ")
        self.credit = float(input("Course credit: "))
        
    def display(self):
        print(f"Course {self.name}, id: {self.id}, credit: {self.credit}")

class Mark():
    def __init__(self):
        self.sid = ""
        self.cid = ""
        self.mark = 0.0
        
    def input(self):
        self.sid = input("Student id: ")
        self.cid = input("Course id: ")
        mark = float(input("Mark: "))
    
        #round-down student scores to 1 digit decimal
        self.mark = math.floor(mark * 10) / 10.0
    
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
    
    def calGPA(self, s_id):
        s_marks = [m for m in self.marks if m.sid==s_id]
        if len(s_marks) == 0:
            return 0.0
        
        marks = []
        credits = []
        
        for m in s_marks:
            for c in self.courses:
                if c.id == m.cid:
                    marks.append(m.mark)
                    credits.append(c.credit)
        
        marks = np.array(marks)
        credits = np.array(credits)

        gpa = np.sum(marks * credits) / np.sum(credits)
        return round(gpa, 2)
    
    def updateGPA(self):
        for s in self.students:
            s.gpa = self.calGPA(s.id)
    
    def sortStudents(self):
        self.updateGPA()
        self.students.sort(key=lambda s: s.gpa, reverse=True)

    def displayStudents(self):
        for s in self.students:
            print(f"{s.name}, ID: {s.id}, dob: {s.dob}, GPA: {s.gpa}")
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

system.displayCourses()
system.displayMarks()

system.updateGPA()
system.sortStudents()
system.displayStudents()
    