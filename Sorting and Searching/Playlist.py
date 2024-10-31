from collections import defaultdict
n=int(input())
arr=list(map(int,input().split()))
c=defaultdict(int)
ans=0
i,j=0,0
 
for j in range(n):
    if arr[j] in c:
        i=max(i,c[arr[j]]+1)
    c[arr[j]]=j
    ans=max(ans,j-i+1)
print(ans)