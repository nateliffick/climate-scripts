# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:17:31 2019

@author: natel
"""
# import the libraries needed
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import tom

# assigning the variable fin to the csv being used
fin="GFS_student.csv"
# reads the csv and makes sure there is a timestamp column
gfs=pd.read_csv(fin,parse_dates=["TIMESTAMP"],index_col=0)
# reads the number of column heads and priints them
gfs.head(10)

# assigning the variable fin to the csv being used
fin="Campus_Met_Data_Daily.csv"
# reads the csv and makes sure there is a timestamp column
obs=pd.read_csv(fin,parse_dates=True,index_col=0)
# reads the number of column heads and priints them
obs.head(10)

# creates the scatter plot
fig,ax=plt.subplots(1,1)
# observing the air temperature average with the 2nd temperature average
ax.scatter(obs["AirTC_Avg"],gfs["2t"],s=1)
# setting the x and y access parameters and limitaions
ax.set_xlim([-5,26])
ax.set_ylim([-5,26])
# labeling the  and y access
ax.set_xlabel("Observed Air Temperature (deg C)")
ax.set_ylabel("Modeled Air Temperature (deg C)")
#assigning grids to the y and y axis
ax.yaxis.grid()
ax.xaxis.grid()
# arrange the number between the two values
x=np.arange(-5,27)
# assign the color black to the points
ax.plot(x,x,color='black')

# the purpose of this script is to examine the bianess of the data whether it is underbiassing, overbiassing, or a perfect representations
# of the daily air temperature values
