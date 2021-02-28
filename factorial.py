#fact=1
#n = int(input('Enter the Number : '))
#for i in range(1,n+1):
#  fact=fact*i
#print(fact)

fact = 1
n = int(input('Enter the number: '))
while n >=1:
  fact=fact*n
  n=n-1
print(fact)

# I made a mistake by defining  n<=0 which is never going to be true 
# 2nd mistake was defining n=n-1 before fact=fact*n