import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def run(self,a,b,c,d):
        if a>b and a>c and a>d:
            if b<c and b<d:
                lowervalue=b
            elif c<b and c<d:
                lowervalue=c
            elif d<b and d<c:
                lowervalue=d
            print("a greatest value"+a+" and d is lowest value" + lowervalue)                 
        elif b>a and b>c and b>d:                
            print("b is greate than a c and d")
        elif c>a and c>d and c>d:                
            print("c is greate than a b and d")
        elif d>a and d>b and d>c: 
            print("d is greate than a b and c")
        return(True)