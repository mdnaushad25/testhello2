import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def run(self,a,b):
        if a>b:
            print("a is greate than b and c")                 
        else:                
            print("c is greate than a and b")
        return(True)
      
                

            
