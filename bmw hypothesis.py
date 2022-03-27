# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 13:31:57 2022

@author: madhan
"""

import pandas as pd

bike=pd.read_excel("C:/Users/madhan/Desktop/bmw bike.xlsx")
bike.head()

from scipy import stats
stats.shapiro(bike.mid age)
stats.shapiro(bike.young age)
stats.ttest_ind(bike.mid,bike.young)
