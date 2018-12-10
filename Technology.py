import numpy as np
import pandas as pd
import datetime

from Commodity_Class import Commodity


class Technology:

    def __init__(self, techName="", fuel=Commodity(), ):
        self.technologyName=techName
        self.fuel= fuel
