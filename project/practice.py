students = [
    {"name": "Anant", "marks": 70},
    {"name": "Dhruv", "marks": 95},
    {"name": "Riya", "marks": 60}
]

sorted_students = sorted(students, key=lambda s: s["marks"], reverse=True)
print(sorted_students)