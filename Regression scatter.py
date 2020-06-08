# -*- coding: utf-8 -*-
"""
This is my analysis script. I can copy/paste all relevant code from
the jupyter notebooks in to this file. When I am ready, I will run it with 
the big green 'play' button at the top of the screeen. I can then inspect 
variables in the "Variable explorer" window (top right); and I can see the output
from my code (e.g. plots) in the IPython console (bottom right).

"""
# Import modules
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import tom

fin="C:/Users/natel/OneDrive/Desktop/Hydro_monitoring/python_code/Campus_Met_Data_Student.csv"
date_parser=lambda x: pd.datetime.strptime(x,"%d/%m/%Y %H:%M")
#obs=pd.read_csv(fin,parse_dates=["TIMESTAMP"],date_parser=date_parser,index_col=0)
obs=pd.read_csv(fin,parse_dates=True,index_col=0)
obs=obs.resample("D").mean()
obs.head(50)

pred,r2 = tom.auto_regress(obs["AirTC_Avg"],obs[["AirTC_Avg","RH"]],2019,1,0.05,True)

pred

fig,ax=plt.subplots(1,1)
ax.scatter(pred["obs"],pred["sim"],s=1)
ax.set_xlim([-5,26])
ax.set_ylim([-5,26])
ax.set_xlabel("Observed Air Temperature (deg C)")
ax.set_ylabel("Modeled Air Temperature (deg C)")
ax.yaxis.grid()
ax.xaxis.grid()
x=np.arange(-5,27)
ax.plot(x,x,color='black')




