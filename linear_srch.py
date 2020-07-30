from array import *

class search :

    def __init__(self,x):
        self.x = x

    def find(self,l,item):
        global i
        flag = False

        for i in range(l):
            if(self.x[i]==item):
                flag = True
                break

        return flag,i

def main():

    a = array('i',[])
    l = int(input("enter the size of the array"))

    for i in range(l):
        x = int(input("enter elmt"))
        a.append(x)

    item = int(input("enter the elmt to be searched"))

    ob = search(a)
    flag,i = ob.find(l,item)

    if(flag==True):
        print("found at ",i)

    else:
        print("not found")

if(__name__=="__main__"):
    main()