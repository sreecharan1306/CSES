# import sys

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n=int(input())
if n==1:
    print(1)
elif n<=3:
    print("NO SOLUTION")
else:
    i,j=1,2
    while j<=n:
        print(j,end=" ")
        j+=2
    while i<=n:
        print(i,end=" ")
        i+=2

