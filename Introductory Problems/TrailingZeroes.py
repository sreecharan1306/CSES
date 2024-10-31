import sys
from math import factorial
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n=int(input())
p=5
ans=0
for _ in range(20):
    ans+=(n//p)
    p*=5
print(ans)