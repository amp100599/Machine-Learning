# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 23:38:58 2019

@author: SAI
"""

import pandas as pd
#from tkinter import Tk,Label


phy_marks=[15,12,8,8,7,7,7,6,5,3]
his_marks=[10,25,17,11,13,17,20,13,9,15]

x=pd.Series(phy_marks)
y=pd.Series(his_marks)

r=x.cov(y)/(x.std()*y.std())
#root=Tk()
#root.title()
#root.geometry("300x300")
#l1=Label(root,text=round(r,3),font='Times 45')
#l1.pack()    

print("Correlation coefficient : %.3f" %r)