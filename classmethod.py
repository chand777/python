class Employee:  
  no_of_leaves=8
  def __init__(self,aname,asalary,arole):
    self.name=aname
    self.salary=asalary
    self.role=arole    
  def printdetails(self):
    return f"Name is {self.name} salary is {self.salary} and role is {self.role}"
    
  @classmethod
  def change_leaves(cls, newleaves):                # This class method we have taken so that we will not required self method 
    cls.no_of_leaves=newleaves
  
sanjay=Employee('Sanjay',500,'Instructor') # to pass the argument you have to create a constructor  
chand=Employee('Chand',1000,'Student')

sanjay.change_leaves(34)
print(sanjay.no_of_leaves)