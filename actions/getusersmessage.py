import sys
import pandas as pd
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self,a,b):
        # c= int(a)+int(b)
        # print("The sum of {0} and {1} is {2}" .format(a, b, c)) 
# num1 = 1.5
# num2 = 6.3
# Add two numbers
        sum = int(a) + int(b)
# Display the sum
        print('The sum of {0} and {1} is {2}'.format(a, b, sum))
        # print(c)
        return(True,sum)