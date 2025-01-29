students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 88},  
    {"name": "Charlie", "score": 92},
    {"name": "Dave", "score": None},   
    {"name": "Eve", "score": 78},
]

print("Grading Students:")
for student in students:
    print(student)
    # if student["score"] is None:  # Stop if a suspicious score is found
    #     print(f"\nSuspicious score detected for {student['name']}! Stopping the grading process.\n")
    #     break
    
    # if student["score"] <= 100:  
    #     print(f"\n{student['name']} scored {student["score"]}.Graded successfully.\n")
    #     continue

    

    print(f"{student['name']} scored {student['score']}. Graded successfully.\n")
