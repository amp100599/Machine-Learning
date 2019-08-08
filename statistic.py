# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 22:08:26 2019

@author: SAI
"""

import pandas as pd
import math

print("enter Elements in array :")

x = list(map(int,input().split()))

array=pd.Series(x)

print("Mean :  %.1f" % array.mean())


print("Median :  %.1f" % array.median())

print("Mode:\n " ,array.mode())
print()

print("Standard deviation : %.1f" % array.std())


n = len(array)
lower = array.mean() - 1.96*array.std()/math.sqrt(n)
higher = array.mean() + 1.96*array.std()/math.sqrt(n)
print("lower limit :",lower)
print("higer limit :",higher)

