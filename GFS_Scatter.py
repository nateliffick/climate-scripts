# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:17:31 2019

@author: natel
"""

import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import tom

fin="C:/Users/natel/OneDrive/Desktop/Hydro_monitoring/python_code/GFS_student.csv"
gfs=pd.read_csv(fin,parse_dates=["TIMESTAMP"],index_col=0)
gfs.head(10)

fin="C:/Users/natel/OneDrive/Desktop/Hydro_monitoring/python_code/Campus_Met_Data_Daily.csv"
obs=pd.read_csv(fin,parse_dates=True,index_col=0)
obs.head(10)

fig,ax=plt.subplots(1,1)
ax.scatter(obs["AirTC_Avg"],gfs["2t"],s=1)
ax.set_xlim([-5,26])
ax.set_ylim([-5,26])
ax.set_xlabel("Observed Air Temperature (deg C)")
ax.set_ylabel("Modeled Air Temperature (deg C)")
ax.yaxis.grid()
ax.xaxis.grid()
x=np.arange(-5,27)
ax.plot(x,x,color='black')

