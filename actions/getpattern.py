import sys
from st2common.runners.base_action import Action
class WritePattern(Action):
    def run(self,a):
        i = 1
        l=1
       
        while i < a:
            while l<a:
                print(" ")
            while i<a:
                print("*")
            i += 1
        return(True)