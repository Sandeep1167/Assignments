n=int(input('enter number:'))
for i in range(1,n+1):
    for j in range(i,i+1):
        print('*'*(n+1-i),end=' ')
    print()
