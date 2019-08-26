import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def run(self,a,b,c,d):
        if a>b and a>c and a>d:
            print("a is greate than b and c")                 
        else:                
            print("c is greate than a and b")
        return(True)