import sys

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

def solve(x):
    return (pow(x,2)*(pow(x,2)-1)//2)-(4*(x-1)*(x-2))
n=int(input())
for i in range(1,n+1):
    print(solve(i),end=" ")