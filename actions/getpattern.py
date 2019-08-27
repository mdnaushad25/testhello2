import sys
from st2common.runners.base_action import Action
class WritePattern(Action):
    def run(self,a):
        p=int(a)
        i = 1    
        for i in range(1,p+1):
            for j in range(1,i+1):
                print("*")
            print("")
            
            
        return(True)