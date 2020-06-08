# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:15:41 2019

@author: natel
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
ax.plot(pred["sim"],color="black",label="SIM")
ax.plot(pred["obs"],color="red",alpha=0.5,label="OBS")
ax.legend()
fig.autofmt_xdate()

ax.set_xlabel("2019 data")
ax.set_ylabel("Temperature (deg C)")

me_sin=np.mean(pred["sim"]-pred["obs"]) 
print("Mean error is: ", me_sin)
mae_sin=np.mean(np.abs(pred["sim"]-pred["obs"])) 
print("Mean absolute error is: ", mae_sin)

#me_sim=np.mean(pred["clim"]-pred["obs"]) 
#print("Mean error is: ", me_sim)
#mae_sim=np.mean(np.abs(pred["clim"]-pred["obs"])) 
#print("Mean absolute error is: ", mae_sim)

me_sim=np.mean(pred["sim"]-pred["clim"]) 
print("Mean error is: ", me_sim)
mae_sim=np.mean(np.abs(pred["sim"]-pred["clim"])) 
print("Mean absolute error is: ", mae_sim)

SS=(1-mae_sin/mae_sim)
print(SS)

