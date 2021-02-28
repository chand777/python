def fibonacci(n):
  n1,n2=0,1
  count=0
  if n < 0:
    print("Invalid Input")
  elif n==1:
    return n1
  else:
    while count <n:
      print(n1,end =" ")
      n1,n2=n2,n1+n2
      count = count +1
print(fibonacci(9))
  