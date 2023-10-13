#!/usr/bin/env python3

def create_grade_report(student_grades):
    with open('reports/grade_report.txt', 'a') as gr:
        for grade in student_grades:
            gr.write(grade + '\n')

#shebang:
if __name__ == '__main__':
    student_grades = []

    grade = input("Student name, grade: ")
    while grade:
        student_grades.append(grade)
        #end when no grade is entered:
        grade = input("Student name, grade: ")

    create_grade_report(student_grades)
    
#the shebang tells the command line that this program should be executed using the Python 3 interpreter

