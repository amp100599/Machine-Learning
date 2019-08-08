# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:01:26 2019

@author: SAI
"""

import numpy as np
from sklearn.linear_model import LinearRegression

x = list(map(int,input().split()))
y = list(map(int,input().split()))

phy_marks = np.array(x).reshape(-1,1)
his_marks = np.array(x).reshape(-1,1)

rm = LinearRegression()
rm.fit(phy_marks,his_marks)

print("Coeff :",rm.coef_)
print("Intercept :",rm.intercept_)

x = int(input("Phy marks:\n"))

his = rm.intercept_ + (x*rm.coef_)
print(round(his,1))
