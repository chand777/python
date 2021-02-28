nterm =int(input('Enter the Number'))
n1,n2=0,1
count=0
if nterm < 1:
  print('Invalid Number')
elif nterm==1:
  print(n1)
else:
  print("Fibonacci Series")
  while count < nterm:
    print(n1,end=" ")
    nth = n1 +n2
    n1 =n2
    n2 =nth
    count = count +1
#0 1 1 2 3 