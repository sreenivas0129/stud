seat=input()

a=input().split(" - ")

e=None

for i in a:

 if seat in i:

 e=i

 break

e=e.split(" ")

lc=e.index(seat)

rc=(len(e)-1)-e.index(seat)

if rc==0:

 rc=99999

print(min([lc,rc]))
