#deserialisation in python
import pickle
class Emp:
    def __init__(self,name,age,esal,eplace):
        self.name=name
        self.age=age
        self.esal=esal
        self.eplace=eplace
    def display(self):
        print(self.name)
        print(self.age)
        print(self.esal)
        print(self.eplace)
f=open('serial.txt','rb') 
e=pickle.load(f)
print('obkect is retriverd successfully')
e.display()