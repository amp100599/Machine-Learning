# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 20:08:33 2019

@author: SAI
"""

import pandas as pd

phy = list(map(int,input().split()))
his = list(map(int,input().split()))

x=pd.Series(phy)
y=pd.Series(his)

r=x.cov(y)/(x.std()*y.std())

beta1 = (r*y.std())/x.std()
print("slope :",round(beta1,3))
