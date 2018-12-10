import numpy as np
import pandas as pd
import datetime

class Commodity:
    
    def _init_(self, isRenewable=False,fuelName=""):
        self.renewable = isRenewable
        self.fuelName=fuelName
        self.prices = pd.DataFrame()
        
        
    def InitialiseArray(self,startDate=datetime.date(2000,1,1),periods=20,frequency="12M",data=np.zeros(),):
        
        dateRange=pd.date_range(startDate,periods=periods,freq=frequency)

        self.prices= pd.DataFrame(data,index=dateRange,columns=self.fuelName)

    def MeanPrices(self,startDate="",endDate=""):

        mean=self.prices[startDate:endDate].mean(axis=0)

        return mean

