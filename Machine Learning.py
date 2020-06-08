# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:44:00 2019

@author: natel
"""

import newtom, pandas as pd, numpy as np
import matplotlib.pyplot as plt

fin="C:/Users/natel/OneDrive/Desktop/Hydro_monitoring/python_code/Campus_Met_Data_Student.csv"
data=pd.read_csv(fin,parse_dates=True,index_col=0)
data=data.resample("D").mean()

fin="C:/Users/natel/OneDrive/Desktop/Hydro_monitoring/python_code/Climatology_mean.csv"
doy_clim=pd.read_csv(fin,parse_dates=["TIMESTAMP"],index_col=0)
doy_clim.head(10)


year_predict=2019
vs=["AirTC_Avg","RH","WS_ms_S_WVT","SlrkW_Avg","NR_Wm2_Avg","BP_mbar_Avg"]

ntrees=100
min_samples=100
pred,mae=newtom.random_forest(target=data["AirTC_Avg"],predictors=data[vs],year_predict=year_predict,days_behind=1,\
                  min_samples=min_samples,ntrees=ntrees)


fig,ax=plt.subplots(1,1)
ax.plot(pred["sim"],color="black",label="SIM")
ax.plot(pred["obs"],color="red",alpha=0.5,label="OBS")
ax.legend()
fig.autofmt_xdate()
ax.set_ylabel("Temperature (deg C)")
ax.set_xlabel("2019 dates")


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


maeref=np.mean(np.abs(pred["clim"]-pred["obs"]))

print(maeref)

ss = 1-(mae/maeref)
print (ss)


