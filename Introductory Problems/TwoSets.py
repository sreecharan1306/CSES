import sys

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n=int(input())
if(n%4==0):
    print("YES")
    a=[]
    b=[]
    for i in range(1,n+1):
        if i%4==3 or i%4==2:
            a.append(i)
        else:
            b.append(i)
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
elif n%4==3:
    print("YES")
    a=[]
    b=[]
    for i in range(1,n+1):
        if i%4==1 or i%4==2:
            a.append(i)
        else:
            b.append(i)
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
else:
    print("NO")