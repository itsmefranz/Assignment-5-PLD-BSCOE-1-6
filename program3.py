age= int(input("Age: "))

if age > -1 and age <= 12:
    print("Kid")
else:
    if age >= 13 and age <= 17:
        print("Teen")
    else:
        if age== 18:
            print("")