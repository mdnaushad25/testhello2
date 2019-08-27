import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def run(self,a,b):        
        a=input("enter the subject:")
        b=input("enter the marks:")
        
        return(True)
    
        