import numpy as np
import pandas as pd
import datetime

from Commodity_Class import Commodity

class RevenueStream:

    def __init__(self, revenueStreamName="", energyPayment=True, capacityPayment=True, energyPrices=Commodity(), capacityPrices=Commodity()):
        self.revenueStream=revenueStreamName
        self.energyPayment=energyPayment
        self.capacityPayment=capacityPayment

        if energyPayment==True:
            self.energyPrices=energyPrices
        else:
            self.energyPrices=0

        if capacityPayment==True:
            self.capacityPrices=capacityPrices
        else:
            self.capacityPrices=0

