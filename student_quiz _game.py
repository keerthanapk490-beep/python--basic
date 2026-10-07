print("Student Quiz Game")

score = 0

answer = input("1. Which programming language are we learning? ")

if answer.lower() == "python":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("2. Which function is used to display output in Python? ")

if answer.lower() == "print":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

answer = input("3. Which symbol is used for assignment in Python? ")

if answer == "=":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("Final Result")
print("Your Score:", score, "/3")
