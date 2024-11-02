import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


def solve(x,y):
    p=max(x,y)
    # a=[i for i in range(pow(p-1,2)+1,pow(p,2)+1)]
    # print(a)
    if x>=y:
        if x&1:
            # return a[y-1]
            return pow(p-1,2)+y
        
        # return a[::-1][y-1]
        return pow(p,2)-y+1
    if y&1:
        return pow(p,2)-x+1
        # return a[::-1][x-1]
    return pow(p-1,2)+x
    
            
for _ in range(int(input())):
    x,y=map(int,input().split())
    print(solve(x,y))