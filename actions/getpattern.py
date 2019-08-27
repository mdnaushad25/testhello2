import sys
from st2common.runners.base_action import Action
class WritePattern(Action):
    def run(self,a):
        # p=int(a)    
        j=a
        p=0   
        for i in range(1,a):
            if p>0:
                for k in range(1,p):
                print(" "),
            for k in range(1,j):
                print("*"),
            j=j-1 
            p=p+1              
            print("\r")           
            
        return(True)