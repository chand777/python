cube =lambda x:x*x*x
def fib(n):
 a,b=0,1
 for i in range(n):
   yield a
   a,b=b,a+b
n=int(input('Enter the number'))
print(list(map(cube,fib(n))))
  
