import sys

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

n=int(input())
mod=int(1e9+7)
print(pow(2,n)%mod)