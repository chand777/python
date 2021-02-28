#classes--->Template
#Object---> Instance of the class
# Why we need class because it uses a concept of DRY: do not repeat yourself 

class Students:
  pass
  
sanjay= Students()  # This are object of Students classs
chand= Students()

#print(sanjay,chand) # it will print two different object

#Let's create a instance Variable 
sanjay.name='sanjay'    # this are the instance variable 
sanjay.std=12
sanjay.section='C'
chand.name='chand'
chand.subjects=['hindi','english','math']

print(sanjay.name,chand.name,chand.subjects)