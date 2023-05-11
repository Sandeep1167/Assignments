#1.print the largest of the three numbers using only if statement
a=int(input('enter number:'))
b=int(input('enter number:'))
c=int(input('enter number:'))
if a>b and a>c:
    print("Large number is:",a)
elif b>a and b>c:
    print("Large number is:",b)
else:
    print("Large number is:",c)
