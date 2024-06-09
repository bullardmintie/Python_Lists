#Task 1 -- Filter out students who have grades below 80
#Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

student_grade = [
    {"students": "John", "grades": 85, "activities": "Football"},
    {"students": "Doe", "grades": 90, "activities": "Music"},
    {"students": "Jane", "grades": 78, "activities": "Art"},
    {"students": "Smith", "grades": 88, "activities": "Dance"},
]

def below_eighty(student_grade):
    return student_grade["grades"] < 80

low_grade = list(filter(below_eighty, student_grade))
print(low_grade)


#Task 2 -- For the remaining students, add students name in a new list named students_approved
#Expected Outcome: students_approved = ["John", "Doe", "Smith"]

def over_eighty(student_grade):
    return student_grade["grades"] >= 80

left_over = list(filter(over_eighty, student_grade))

students_approved = [x for x in students if x != "Jane"]


#Task 3 -- Print the list students_approved

print(students_approved)