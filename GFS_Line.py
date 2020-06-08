# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:19:26 2019

@author: natel
"""
# importing the libraries needed
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import tom

# setting the variables for the csv file
fin="weather.csv"
# read the csv and make sure it has the column timestamp on it
gfs=pd.read_csv(fin,parse_dates=["TIMESTAMP"],index_col=0)
# check the number of headings it has
gfs.head(10)

# Setting another variable for a differnt csv file
fin="Climatology.csv"
# reading the file for timestamp column
doy_clim=pd.read_csv(fin,parse_dates=["TIMESTAMP"],index_col=0)
# printing out how many columns there is
doy_clim.head(10)

# setting the plot up
fig,ax=plt.subplots(1,1)
# creating the labels and colors of the plot line
ax.plot(doy_clim["obs"],color="black",label="Observed")
# creating the labels and colors of the plot line
ax.plot(gfs["2t"],color="red",alpha=0.5,label="gfs")
# creating the labels and colors of the plot line
ax.plot(doy_clim["clim"],color="silver",alpha= 1,label="clim")
# adding the legend 
ax.legend()
fig.autofmt_xdate()

# creating the second line plot inside of the original plot
fig,ax=plt.subplots(1,1)
# creating the label for the secondary lines in the original plot 
ax.plot(doy_clim.loc[doy_clim.index.year==2019]["obs"],color="black",label="Observed")
# creating the label for the secondary lines in the original plot 
ax.plot(gfs.loc[gfs.index.year==2019]["2t"],color="red",alpha=1,label="gfs")
# creating the label for the secondary lines in the original plot 
ax.plot(doy_clim.loc[doy_clim.index.year==2019]["clim"],color="yellow",alpha= 1,label="clim")
# setting up the legend format
ax.legend()
fig.autofmt_xdate()
# format for the x and y labels 
ax.set_xlabel("2019 data")
ax.set_ylabel("Modeled Air Temperature (deg C)")


# comparing the sinisoudal curve of the two differnt line means and printing out the mean and mean absolute error
me_sin=np.mean(gfs["2t"]-doy_clim["obs"]) 
print("Mean error is: ", me_sin)
mae_sin=np.mean(np.abs(gfs["2t"]-doy_clim["obs"])) 
print("Mean absolute error is: ", mae_sin)

#comparing the sinisoudal curve of the two differnt line means and printing out the mean and mean absolute error
# this is used to figure out what type of model is a better fit for the weather data being observed 
me_r=np.mean(doy_clim["clim"]-doy_clim["obs"]) 
print("Mean error is: ", me_r)
mae_r=np.mean(np.abs(doy_clim["clim"]-doy_clim["obs"])) 
print("Mean absolute error is: ", mae_r)

# calculates the skill score of the model the closer to 1 proves the origional model is a better model 
# closer to -1 illustrates the new model is a more accurate model 
print (1-mae_sin/mae_r)



