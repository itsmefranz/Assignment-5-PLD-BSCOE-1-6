def gradePercentage():
    percentage= float(input("Please indicate students' percentage: "))
    return percentage

grade= gradePercentage()

if grade >= 97 and grade == 100:
    print("Grade/Mark: 1.0")
    print("Description: Excellent")
else:
    if grade >= 94 and grade <= 96:
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
    else:
        if grade >= 91 and grade <=93:
            print("Grade/Mark: 1.5")
            print("Description: Very Good")
        else:
            if grade >= 88 and grade <= 90:
                print("Grade/Mark: 1.75")
                print("Description: Very Good")
            else:
                if grade >= 85 and grade <= 87:
                    print("Grade/Mark: 2.0")
                    print("Description: Good")
                else:
                    if  grade >= 65 and  grade <= 74:
                        print("Grade/Mark: 5.0")
                        print("Description: Failure")
                    else:
                        if grade == 75:
                            print("Passing")