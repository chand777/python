# Alternate Constructor
class Employee:  
  no_of_leaves=8
  def __init__(self,aname,asalary,arole):    # this is constructor 
    self.name=aname
    self.salary=asalary
    self.role=arole    
  def printdetails(self):
    return f"Name is {self.name} salary is {self.salary} and role is {self.role}"
    
  @classmethod
  def change_leaves(cls, newleaves):                # This class method we have taken so that we will not required self method 
    cls.no_of_leaves=newleaves

  @classmethod
  def from_dash(cls, string):
    # param = string.split("-")
    # return cls(param[0],param[1],param[2])
    return cls(*string.split('-'))



  
# sanjay=Employee('Sanjay',500,'Instructor') # to pass the argument you have to create a constructor  
# chand=Employee('Chand',1000,'Student')
duck =Employee.from_dash("duck-000-nothing")
# sanjay.change_leaves(34)
# print(sanjay.no_of_leaves)
print(duck.role)