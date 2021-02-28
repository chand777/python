#Multiply Inheritance

class Dad:

   basketball=1

  
class Son(Dad):
  dance = 1
  
  def isdance(self):
    return f"Yes I dance {self.dance} no. of times"
  
class Grandson(Son):
  dance =6
  
  # def isdance(self):
    # print("This is Test")
    # return f" I'm awesome dancer and I dance {self.dance} no. of times"
    
    
    
daddy=Dad()
chand=Son()
tom=Grandson()

# print(tom.isdance())
print(tom.basketball)
  

  