import sys
from st2common.runners.base_action import Action

class getusersmessage(Action):

    def run(self,a,b):
        print(type(a),type(b))
        sum=a + b
        print(sum)
        return(True,sum)