#Program 2: Find the lowest number
#Create a program that ask 3 numbers.
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))

smallest= 0

#Find the lowest number using only if-else statement.
if a<b and a<c:
    smallest= a
else:
    if b<a and b<c:
        smallest= b
    else:
        if c<a and c<b:
            smallest= c

#Display the lowest number
print(f'{smallest}, is the smallest of the three numbers.')