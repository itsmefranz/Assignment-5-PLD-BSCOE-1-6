a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))

smallest= 0

if a<b and a<c:
    smallest= a
else:
    if b<a and b<c:
        smallest= b
    else:
        if c<a and c<b:
            smallest= c

print(f'{smallest}, is the smallest of the three numbers.')