import sys
from st2common.runners.base_action import Action
class MyAction(Action):
    def isNumber(self,s) :       
        for i in range(len(s)) : 
            if s[i].isdigit() != True : 
                return False
        return True
    def run(self,a,b,c,d,e):
        dictionary1 = dict() 
        dictionary1.update({a:a})
        bvalue=b
        cvalue=c
        dvalue=d
        evalue=e
        aa=1
        bb=1
        if self.isNumber(bvalue):
            dictionary1.update({a:bvalue})
            aa=aa+1
        else:
            dictionary1.update({a:{bvalue:bvalue}})
            bb=bb+1

        if aa==2:
            if self.isNumber(cvalue):
                # dictionary1.update({a:bvalue,cvalue:cvalue})
                # aa=aa+1
                print("is not valid sequence...")
            else:
                dictionary1.update({a:bvalue,cvalue:cvalue})
                aa=aa+1
        if bb==2:
            if self.isNumber(cvalue):
                dictionary1.update({a:{bvalue:cvalue}})
                bb=bb+1
            # else:
            #     dictionary1.update({a:{bvalue:bvalue,cvalue:cvalue}})
            #     bb=bb+1
        if aa==3:
            if self.isNumber(dvalue):
                dictionary1.update({a:bvalue,cvalue:dvalue})
                aa=aa+1
            else:
                dictionary1.update({a:bvalue,cvalue:{dvalue:dvalue}})
                aa=aa+1
        if bb==3:
            if self.isNumber(dvalue):
                print("no. is not valid")
            else:
                dictionary1.update({a:{bvalue:cvalue,dvalue:dvalue}})
                bb=bb+1
            
        if bb==4:
            if self.isNumber(evalue):
                dictionary1.update({a:{bvalue:cvalue,dvalue:evalue}})
                bb=bb+1
        if aa==4:
            if self.isNumber(evalue):
                dictionary1.update({a:bvalue,cvalue:{dvalue:dvalue}})
                aa=aa+1                
            else:
                dictionary1.update({a:bvalue,cvalue:dvalue,evalue:evalue})
                aa=aa+1
        # dictionary1.update({a: {b:c,d:e}})
         
        # print(dictionary1) 
        return(True,dictionary1)
    