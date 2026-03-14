
# Task 1: Create a Dictionary of Student Marks

stud_marks_data={"John":  85,
                 "Nik":  80,
                 "Ashu": 75,
                 "Priya": 95,
                 "Rano": 71}

see_marks=input("Enter the student's name:")

if see_marks in stud_marks_data:
    print(f"{see_marks} marks: {stud_marks_data[see_marks]}")
else:
    print(f"Student name: {see_marks} not found!")

# Task 2: Demonstrate List Slicing

num=list(range(1,11))
print(f"Original list: {num}")

new_lst=num[:5]
print(f"Extreact first five elements: {new_lst}")

new_lst.reverse()
print(f"Reversed extracted elements: {new_lst}")


