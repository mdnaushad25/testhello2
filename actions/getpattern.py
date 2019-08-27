import sys
from st2common.runners.base_action import Action
class WritePattern(Action):
    def run(self,a):
        # p=int(a)    
        j=a    
        for i in range(1,a):
            for k in range(1,j):
                print("*"),
            
            print("\r")           
            
        return(True)