import sys
from collections import defaultdict,Counter
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

def solve(s,p):
    oodd=False
    oc='a'
    of=0
    a,b=[],[]
    for ch,count in p.items():
        if count&1:
            if oodd:
                return "NO SOLUTION"
            else:
                oodd=True
                oc=ch
                of=count
        else:
            for _ in range(count//2):
                a.append(ch)
                b.append(ch)
    if oodd:
        for _ in range(of//2):
            a.append(oc)
            b.append(oc)
        a.append(oc)
    # print(a)
    # print(b)
    ans=''.join(a)+''.join(b[::-1])
    return ans
            
    
        
s=input()
p=Counter(s)
# print(p)
print(solve(s,p))
        