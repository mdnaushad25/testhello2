import sys
from st2common.runners.base_action import Action
class WritePattern(Action):
    def run(self,a):
        i = 1
        j = 1       
        for i in range(i,a+1):
            for j in range(j,i+1):
                print("*")
            print()
            
            
        return(True)