import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# 
n=int(input())
while n!=1:
    print(n,end=" ")
    if n&1:
        n=n*3+1
    else:
        n//=2
print(1)
