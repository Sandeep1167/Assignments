'''1 n=int(input('enter number:'))
    for i in range(1,n+1):
        for j in range(i,i+1):
            print('*'*(n+1-i),end=' ')
        print()'''

''' 4n=int(input('enter number:'))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end='')
        print()'''

n=int(input('enter number:'))
for i in range(1,n+1):
    for j in range(i,n+1):
        print(i,end='')
    print()