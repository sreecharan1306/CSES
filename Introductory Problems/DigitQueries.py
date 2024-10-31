import sys

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

s=""
for i in range(1,1001):
    s+=str(i)
n=int(input())
for _ in range(n):
    k=int(input())
    print(s[k-1])