from rich.console import Console
from rich.table import Table

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Subject:
    def __init__ (self, sub_name, credit):
        self.name = sub_name
        self.credit = credit
        self.students = {}
        self.average = 0

    def add_student(self, student):
        self.students[student] = []

    def add_grade(self, student, grade):
        self.students[student].append(grade)

    def get_average(self, student):
        total = 0
        for grade in self.students[student]:
            total += grade
        self.average = total / len(self.students[student])
        return self.average

    def grades(self, student):
        return self.students[student]

p1 = Student("Dovydas", 21)
p2 = Student("Sofia", 21)
p3 = Student("Nedas", 21)
p4 = Student("Viktorija", 21)

s1 = Subject("Python", 6)
s1.add_student(p1)
s1.add_grade(p1, 9)
s1.add_grade(p1, 10)
s1.add_grade(p1, 9)
s1.add_grade(p1, 8)
s1.add_grade(p1, 10)

s2 = Subject("Mobiliosios programeles", 6)
s2.add_student(p2)
s2.add_grade(p2, 10)
s2.add_grade(p2, 10)
s2.add_grade(p2, 10)
s2.add_grade(p2, 9)
s2.add_grade(p2, 8)

s3 = Subject("Hibridines mobiliosios programeles", 6)
s3.add_student(p3)
s3.add_grade(p3, 8)
s3.add_grade(p3, 8)
s3.add_grade(p3, 9)
s3.add_grade(p3, 10)
s3.add_grade(p3, 10)

s4 = Subject("3D grafika", 3)
s4.add_student(p4)
s4.add_grade(p4, 10)
s4.add_grade(p4, 10)
s4.add_grade(p4, 10)
s4.add_grade(p4, 10)
s4.add_grade(p4, 10)

table = Table(title="Students")

rows = [
    [p1.name, str(p1.age), s1.name, str(s1.credit), str(s1.grades(p1)), str(s1.get_average(p1))],
    [p2.name, str(p2.age), s2.name, str(s2.credit), str(s2.grades(p2)), str(s2.get_average(p2))],
    [p3.name, str(p3.age), s3.name, str(s3.credit), str(s3.grades(p3)), str(s3.get_average(p3))],
    [p4.name, str(p4.age), s4.name, str(s4.credit), str(s4.grades(p4)), str(s4.get_average(p4))],
]

columns = ["First Name", "Age", "Subject", "Credit", "Marks", "In total"]

for column in columns:
    table.add_column(column)

for row in rows:
    table.add_row(*row)

console = Console()
console.print(table)
