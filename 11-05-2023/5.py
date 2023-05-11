#5.program to check student grades
marks=int(input('Enter marks:'))
if marks<=500 and marks>=600:
    print('A Grade')
elif marks<=400 and marks >=499:
    print('B Grade')
elif marks<=300 and marks >=399:
    print('C Grade')
elif marks<250:
    print('Fail')
else:
    print('Enter valid marks')