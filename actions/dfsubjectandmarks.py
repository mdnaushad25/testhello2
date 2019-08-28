import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def isNumber(self,s) :       
        for i in range(len(s)) : 
            if s[i].isdigit() != True : 
                return False
        return True
    def run(self,a,b,c,d,e): 
        bvalue=b
        if self.isNumber(bvalue):
            print("integer")
        else:
            print("string")

        dictionary1 = dict()
        
        dictionary1.update({a: {b:c,d:e}})
        # dictionary1.update({a: {d:e}})   
        # print("Student Subject and marks") 
    
        # print(dictionary1) 
        return(True,dictionary1)
    