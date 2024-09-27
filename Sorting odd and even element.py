n=int(input())

l=list(map(int,input().split()))

res=[]

for i in l:

 if i%2==0:

 res.append(i)

for i in l:

 if i not in res:

 res.append(i)

print(res)
