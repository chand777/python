# reuseability 
class Employee:  
  no_of_leaves=8
  def __init__(self,aname,asalary,arole):
    self.name=aname
    self.salary=asalary
    self.role=arole    
  def printdetails(self):
    return f"Name is {self.name} salary is {self.salary} and role is {self.role}"
    
  
sanjay=Employee('Sanjay',500,'Instructor') # to pass the argument you have to create a constructor  
#chand=Employee()

# sanjay.name='Sanjay'
# sanjay.salary=500
# sanjay.role='Instructor'



# chand.name='Chand'
# chand.salary=400
# chand.role='student'

print(sanjay.printdetails())
#print(chand.no_of_leaves)
print(sanjay.salary)