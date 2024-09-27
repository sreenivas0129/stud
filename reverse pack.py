n=int(input())

a=list(map(int,input().split()))

d={}

for i in a:

 if i not in d:

 d[i]=1

 else:

 d[i]+=1

res=[]

for key,val in d.items():

 res+=[val]*key

res.sort()

print(res)
