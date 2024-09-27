def fib(n,memo={}):

 if n==0 or n==1:

 return 1

 if n in memo:

 return memo[n]

 res=(fib(n-1,memo)**2+fib(n-2,memo)**2)%47

 memo[n]=res

 return res

n=int(input())

print(fib(n))
