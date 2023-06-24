import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddy']

student_scores = {student: random.randint(1, 100) for student in names}

passing_students = {student: score for (student, score) in student_scores.items() if score >= 60}

print(passing_students)
