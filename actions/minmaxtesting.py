import sys
from st2common.runners.base_action import Action
class minmaxclass(Action):
    def checkminmax(self,a,b,c):
        if a>b:
            if a>c:
                print("a is greate than b and c")
            else:
                print("c is greate than a and b")
        elif b>c:
            print("b is greater than a and c")
            else:
                print("c is greater than a nad b")
                

            
