# prime

class prime:
  def __init__(self):
    self.n = 0
  def inp(self):
    self.n = int(input("enter a number")
  def find(self):
    b = True
    for i in range(2,self.n):
      if(self.n%i==0):
        b = False
        break
    return b
ob = prime()
ob.inp()
b = ob.find()
if(b == True):
  print("primt")
else:
  print("not prime")
