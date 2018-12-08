# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 22:05:18 2018

@author: Sanjay
"""
import datetime
import numpy as np
import pandas as pd


a=datetime.date(2001,1,1)
b=datetime.timedelta(10)
#print(a)

#print(a+b)

c=pd.date_range(a,periods=10,freq = "Y")
#print(c)

d=pd.DataFrame(np.zeros((10,1)),index=c, columns=list("A"))

#print(d)

Prices = pd.DataFrame()

print(Prices)

Prices=d

print(Prices)

data=np.array(0)

print(data)