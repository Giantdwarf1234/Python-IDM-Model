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

data =np.array([1,2,3,4,5,6,7,8,9,10])

c=pd.date_range(a,periods=10,freq = "12M")
#print(c)

d=pd.DataFrame(data,index=c, columns=list("A"))

#print(d)

Prices = pd.DataFrame()

#print(Prices)

Prices=d

#print(Prices)

#print(data)

mean=Prices["2001-01-31":"2003-01-31"].mean(axis=0)

print(mean)

