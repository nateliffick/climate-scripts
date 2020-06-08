# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:44:00 2019

@author: natel
"""
# import the libraries needed
import newtom, pandas as pd, numpy as np
import matplotlib.pyplot as plt

# assigns the variable to the csv file needed
fin="Campus_Met_Data_Student.csv"
# read the csv file
data=pd.read_csv(fin,parse_dates=True,index_col=0)
# resamples the mean data 
data=data.resample("D").mean()

# assigns the variable to the csv file needed
fin="Climatology_mean.csv"
# read the csv file
doy_clim=pd.read_csv(fin,parse_dates=["TIMESTAMP"],index_col=0)
# reads all the column head in the csv file
doy_clim.head(10)

# sets the year to the variable in order to help predict future air temperatures 
year_predict=2019
#assigns the var to the columns needed to predict future temp
vs=["AirTC_Avg","RH","WS_ms_S_WVT","SlrkW_Avg","NR_Wm2_Avg","BP_mbar_Avg"]

# number of trees for the machine learning algo
ntrees=100
# number of samples for the ml algo
min_samples=100
# the columns and variables in the csv the ml program will look directly at 
pred,mae=newtom.random_forest(target=data["AirTC_Avg"],predictors=data[vs],year_predict=year_predict,days_behind=1,\
                  min_samples=min_samples,ntrees=ntrees)

# creates a plot
fig,ax=plt.subplots(1,1)
# assigns what data is going to be plotted as well as color and label
ax.plot(pred["sim"],color="black",label="SIM")
ax.plot(pred["obs"],color="red",alpha=0.5,label="OBS")
# creates a legend box
ax.legend()
# auto formates the date on the x axis
fig.autofmt_xdate()
# assigns the labels to the x and y axis
ax.set_ylabel("Temperature (deg C)")
ax.set_xlabel("2019 dates")

# creates a plot
fig,ax=plt.subplots(1,1)
# creates a scatter plot 
ax.scatter(pred["obs"],pred["sim"],s=1)
# sets the x and y axis limits for the scatter plots
ax.set_xlim([-5,26])
ax.set_ylim([-5,26])
# labels the x and y axis for the scatter plot
ax.set_xlabel("Observed Air Temperature (deg C)")
ax.set_ylabel("Modeled Air Temperature (deg C)")
# adds the crid lines for both the x and y axis
ax.yaxis.grid()
ax.xaxis.grid()
# tells the plot where the scatter plot data should fall between
x=np.arange(-5,27)
# assigns the plot dot points to black
ax.plot(x,x,color='black')

# assigns the new variable to accurately predict the future mean air temps
maeref=np.mean(np.abs(pred["clim"]-pred["obs"]))
# prints the new predicted mean for air temp
print(maeref)

# creates the equation to calculate the skillscore
ss = 1-(mae/maeref)
# prints the skillscore
print (ss)


