student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermonie":99,
    "Draco":74,
    "Neville":62,
    }


#TODO 1: create an empty dict student grades
student_grade = {}


#TODO 2: write your code below to add the grades to student grades
for student in student_scores:
    student_grade[student] = student
    
for students in student_grade:
    if student_scores[students] >=91:
        student_grade[students] = "Outstanding"
    elif student_scores[students] >=81:
        student_grade[students] = "Exceeds Expectation"
    elif student_scores[students] >=71:
        student_grade[students] = "Acceptable"
    else:
        student_grade[students] = "Fail"
        
print(student_grade)


