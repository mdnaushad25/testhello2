import sys
from st2common.runners.base_action import Action
class WritePattern(Action):
    def run(self,a):
        # p=int(a)        
        for i in range(1,a):
            for j in range(1,i+1):
                print("*")
            print("\r")
            
            
        return(True)