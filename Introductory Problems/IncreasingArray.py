# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n=int(input())
arr=list(map(int,input().split()))
ans=0
for i in range(1,n):
    if arr[i-1]>arr[i]:
        ans+=(abs(arr[i-1]-arr[i]))
        arr[i]=arr[i-1]
    
print(ans)