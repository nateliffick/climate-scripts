# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:19:26 2019

@author: natel
"""

import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import tom

fin="C:/Users/natel/OneDrive/Desktop/Hydro_monitoring/python_code/GFS_student.csv"
gfs=pd.read_csv(fin,parse_dates=["TIMESTAMP"],index_col=0)
gfs.head(10)

fin="C:/Users/natel/OneDrive/Desktop/Hydro_monitoring/python_code/Climatology_mean.csv"
doy_clim=pd.read_csv(fin,parse_dates=["TIMESTAMP"],index_col=0)
doy_clim.head(10)

fig,ax=plt.subplots(1,1)
ax.plot(doy_clim["obs"],color="black",label="Observed")
ax.plot(gfs["2t"],color="red",alpha=0.5,label="gfs")
ax.plot(doy_clim["clim"],color="silver",alpha= 1,label="clim")
ax.legend()
fig.autofmt_xdate()


fig,ax=plt.subplots(1,1)
ax.plot(doy_clim.loc[doy_clim.index.year==2019]["obs"],color="black",label="Observed")
ax.plot(gfs.loc[gfs.index.year==2019]["2t"],color="red",alpha=1,label="gfs")
ax.plot(doy_clim.loc[doy_clim.index.year==2019]["clim"],color="yellow",alpha= 1,label="clim")
ax.legend()
fig.autofmt_xdate()
ax.set_xlabel("2019 data")
ax.set_ylabel("Modeled Air Temperature (deg C)")



me_sin=np.mean(gfs["2t"]-doy_clim["obs"]) 
print("Mean error is: ", me_sin)
mae_sin=np.mean(np.abs(gfs["2t"]-doy_clim["obs"])) 
print("Mean absolute error is: ", mae_sin)

me_r=np.mean(doy_clim["clim"]-doy_clim["obs"]) 
print("Mean error is: ", me_r)
mae_r=np.mean(np.abs(doy_clim["clim"]-doy_clim["obs"])) 
print("Mean absolute error is: ", mae_r)

print (1-mae_sin/mae_r)



