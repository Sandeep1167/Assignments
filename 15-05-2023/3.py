'''
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
n=int(input('enter number:'))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j,end='')
    print()
