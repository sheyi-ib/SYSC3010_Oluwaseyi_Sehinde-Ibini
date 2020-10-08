import random

#temperature module class 
class tempMod:
    def readC(self):
        return random.randint(10,22)

#display module class
class dispMod:
    def Print(self,s):    
        print(f'| {s}\r', end="")

    def init(self):
        print("\n\n|---------------|")