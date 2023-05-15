n=int(input('enter number:'))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n-j+1,end='')
    print()