n=int(input())

a=list(map(int,input().split()))

sm=0

for i in a:

 if i>=5:

 sm+=i

print(sm)
