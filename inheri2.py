class Employee:  
  no_of_leaves=8
  var=9
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





  @staticmethod                                           # to increase the efficiency and the excecute only this block we will use static and class method
  def printgood(string):
    print("This is good " + string)

class Player:
  var=9
  no_of_games = 4
  def __init__(self,name,game):
    self.name=name
    self.game=game
    
  def printdetails(self):
    return f"Name is {self.name} game is {self.game}"
    

class Coolprogramer(Employee,Player):
  var=10
  language='C++'
  def lang(self):
    print(self.language)



sanjay=Employee('Sanjay',500,'Instructor') # to pass the argument you have to create a constructor  
chand=Employee('Chand',1000,'Student')
duck =Employee.from_dash("duck-000-nothing")

tom= Player('TOM',['Football','Football','Football'])
sekar=Coolprogramer('Sekar',777,'coolprog')

print(sekar.lang())

