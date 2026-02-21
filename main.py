import csv
import os

def load_students():
    students = []

    
    filepath = os.path.join("students", "glourvell_university_students.csv")

    with open(filepath, mode='r') as student_records:
        reader = csv.DictReader(student_records)
        for row in reader:
            
            student = dict(row)  
            students.append(student)

    return students


students = load_students()
for student in students:
    print(student)