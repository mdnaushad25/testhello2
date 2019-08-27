import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def run(self,a,b):
        allvalue="Subject: "+a+"  Marks: "+b
        print(allvalue)
        return(True)
    
        