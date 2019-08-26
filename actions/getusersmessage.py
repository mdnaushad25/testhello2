import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self,a,b):
        var1:int=a
        var2:int=a
        var3=var1+var2     
        print(var3)
        return(True,var3)