import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def run(self,a,b,c,d):
        #Dictionary1 = {'A': 'Geeks', 'B': 'For'}     
        # Printing keys of dictionary 
        dictionary1 = dict()
        dictionary1.update({a: b})
        dictionary1.update({c: d})   
        print("Keys before Dictionary Updation:") 
        #keys = Dictionary1.keys() 
       # print(keys) 
        print(dictionary1) 
        return(True,dictionary1)
    
        