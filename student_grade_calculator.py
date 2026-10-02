print("===== Student Grade Calculator =====")

name = input("Enter your name: ")

maths = float(input("Enter Maths mark: "))
python = float(input("Enter Python mark: "))
english = float(input("Enter English mark: "))
science = float(input("Enter Science mark: "))
computer = float(input("Enter Computer Science mark: "))

total = maths + python + english + science + computer
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Result =====")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
