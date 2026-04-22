# Task 5 — Dictionaries

student = {"name": "Ada", "grade": 92, "subjects": ["math", "cs"]}
print(student["name"])
print(student.get("grade"))
for key, value in student.items():
    print(f"{key}: {value}")
