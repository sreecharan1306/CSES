import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def solve(a,b,s):
    # print(*s)
    if a==0 and b==0:
        return "YES"
    if a==0 or b==0:
        return "NO"
    
    p=min(a,b)
    q=max(a,b)
    if p*2<q:
        return "NO"
    if (a+b)%3==0:
        return "YES"
    return "NO"
s=[0]*105
# s[1]=1
# i=2
# for _ in range(100):
#     s[i]=s[i-1]+s[i-2]
#     i+=1
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(solve(a,b,s))
