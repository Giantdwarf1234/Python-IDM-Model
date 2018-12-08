import numpy as np
import pandas as pd

class Fuel:
    
    def _init_(self, isRenewable=False,fuelName=""):
        self.renewable = isRenewable
        self.fuelName=fuelName
        self.prices = pd.DataFrame()
        
        
    def InitialiseArray(self,dates=pd.date_range(),data=np.zeros(),):
        
        self.prices= pd.DataFrame(data,index=dates,column)
        
        