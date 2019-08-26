import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def run(self,a,b,c,d):
        if a>b and a>c and a>d:
            print("a is greate than b c and d")                 
        elif b>a and b>c and b>d:                
            print("b is greate than a c and d")
        elif c>a and c>d and c>d:                
            print("c is greate than a b and d")
        else
            print("d is greate than a b and c")
        return(True)