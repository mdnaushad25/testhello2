import sys
from st2common.runners.base_action import Action

class getusersmessage(Action):

    def run(self,a,b):
        sum=int(a)+int(b) 
        print(sum)
        return(True,sum)