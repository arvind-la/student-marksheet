def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "Fail"

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

marks = []
subjects = ["Maths", "Physics", "Chemistry", "English", "Computer Science"]

for subject in subjects:
    score = int(input(f"Enter marks for {subject}: "))
    marks.append(score)

total = sum(marks)
average = total / len(marks)
grade = calculate_grade(average)

print("\n----- Marksheet -----")
print("Name:", name)
print("Roll No:", roll_no)
for i in range(len(subjects)):
    print(f"{subjects[i]}: {marks[i]}")
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
