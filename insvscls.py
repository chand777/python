#Instance variable Vs Class Variable
class Employee:  # it is good to give calss name in capital letter 
  no_of_leaves=8   # this will be same for sanjay and chand
  pass
  
sanjay=Employee()
chand=Employee()

sanjay.name='Sanjay'
sanjay.salary=500
sanjay.role='Instructor'



chand.name='Chand'
chand.salary=400
chand.role='student'

print(chand.no_of_leaves) # here we are accessing variable of class with object of chand
print(Employee.no_of_leaves) # you can access the class variable with class also 

Employee.no_of_leaves=9
print(Employee.no_of_leaves) # you can change class variable with class name only

print(chand.__dict__) # it will give cahnd name salary and role not the number of leaves
chand.no_of_leaves=12  # it will create new instance variable of chand 
print(chand.__dict__) # it will give chand name salary and role and number of leaves because we have created instance variable above 
print(Employee.no_of_leaves) # It will print 9
print(Employee.__dict__)

#Note only class can change it's variable but you can acces the class variable with instance 

