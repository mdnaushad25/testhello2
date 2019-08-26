import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self,a,b):
        c= int(a)+int(b)
        print("The sum of {0} and {1} is {2}" .format(a, b, c)) 

        # print(c)
        return(True,c)