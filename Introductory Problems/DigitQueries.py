import sys
from collections import defaultdict
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

s=""
for i in range(1,1001):
    s+=str(i)
n=int(input())
mp=defaultdict(list)
for i,e in enumerate(s):
    # print(i,e)
    mp[e].append(i)
for i,j in mp.items():
    print(i,"-->",j)
for _ in range(n):
    k=int(input())
    # print(s[k-1])