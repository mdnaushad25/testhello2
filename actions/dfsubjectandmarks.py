import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def run(self,a,b,c,d,e):     
        dictionary1 = dict()
        dictionary1.update(a: {b:c})
        dictionary1.update(a: {d:e})   
        print("Student Subject and marks") 
    
        print(dictionary1) 
        return(True,dictionary1)
    