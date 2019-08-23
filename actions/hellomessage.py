import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, message):
        message="hi how are you. very soon give me information"
        print(message)
        return(True,message)