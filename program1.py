def gradePercentage():
    percentage= float(input("Please indicate students' percentage: "))
    return percentage

corres= gradePercentage()

if grade >= 65 and  grade <= 74:
    print("Grade/Mark: 5.0")
    print("Description: Failure")
elif grade == 75:
    print("Passing")