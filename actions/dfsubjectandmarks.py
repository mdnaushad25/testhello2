import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def isNumber(self,s) :       
        for i in range(len(s)) : 
            if s[i].isdigit() != True : 
                return False
        return True
    def run(self,a,b,c,d,e):
        variable = [a,b,c,d,e]
        dictionary1 = dict() 
        for i in variable:
            print(i)
        # dictionary1.update({a:a})
        # variable=b
        # variable=c
        # variable=d
        # variable=e
        print(variable)
        # if self.isNumber(bvalue):
        #     variable=bvalue
        # else:
        #     variable=bvalue

        
        # dictionary1.update({a: {b:c,d:e}})
         
        # print(dictionary1) 
        return(True,variable)
    