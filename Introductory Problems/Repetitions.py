import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

s=input()
ans=1
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        c=1
    ans=max(ans,c)
        
print(ans)