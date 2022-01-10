#Program 2: Find the lowest number
#Create a program that ask 3 numbers.
first_num= int(input("Enter first number: "))
second_num= int(input("Enter second number: "))
third_num= int(input("Enter third number: "))

smallest= 0

#Find the lowest number using only if-else statement.
if first_num < second_num and first_num < third_num:
    smallest= first_num
else:
    if second_num< first_num and second_num< third_num:
        smallest= second_num
    else:
        if third_num<first_num and third_num<second_num:
            smallest= third_num

#Display the lowest number
print(f'{smallest}, is the smallest of the three numbers.')