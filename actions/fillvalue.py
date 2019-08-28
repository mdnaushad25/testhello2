import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def run(self,a,b):
        Dictionary1 = {'A': 'Geeks', 'B': 'For'}     
        # Printing keys of dictionary 
        print("Keys before Dictionary Updation:") 
        keys = Dictionary1.keys() 
        print(keys) 
        print(Dictionary1) 
        return(True)
    
        