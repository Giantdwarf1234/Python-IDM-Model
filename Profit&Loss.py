import numpy as np
import pandas as pd
import datatime


class ProfitAndLoss:
    
    def _init__(self,operatingLife=0, developmentTime=0, startDate=datetime.date(2000,0,1),capexArray=pd.DataFrame(), opexArray=pd.DataFrame(), revenues=pd.DataFrame()):
        self.projectlife = operatingLife + developmentTime
        self.dates=pd.date_range(startDate,periods=operatingLife+developmentTime, freq="Y")
        self.P&L = pd.DataFrame(np.zeros((operatingLife+developmentTime,1) ),index=dates)