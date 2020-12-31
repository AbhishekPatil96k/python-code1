#serialissation in python
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
e=Emp('ramu',24,2014,'banglore')
with open('serial.txt','wb') as f:
    pickle.dump(e,f)
print('object is stored in files')
        