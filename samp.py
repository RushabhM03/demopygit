# prime

class prime:

  def __init__(self):
    self.n = 0

  def inp(self):
    self.n = int(input("enter a number"))

  def check(self):
    flag = True
    for i in range(2,self.n):
      if(self.n&i==0):
        flag = False
        break
    return flag

def main():
  ob = prime()
  ob.inp()
  b = ob.check()

  if(b == True):
    print("prime")
  else:
    print("not prime")

main()
