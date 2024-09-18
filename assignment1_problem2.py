student_name = input("Please enter your student name: ")
student_point = int(input("Please enter your student point: "))

print(f"Welcome {student_name}! your point is {student_point}")

grade = ""
if student_point >= 85 and student_point <= 100:
    grade = "A"
elif student_point >= 75 and student_point <= 84:
    grade = "B"
elif student_point >= 65 and student_point <= 74:
    grade = "C"
elif student_point >= 55 and student_point <= 64:
    grade = "D"
elif student_point >= 0 and student_point <= 54:
    grade = "E"
else:
    grade = "invalid, because of range point"

print(f"Your grade is {grade}")