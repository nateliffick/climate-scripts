# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:15:41 2019

@author: natel
"""

# Import modules
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import tom

# assign the fin variable to the csv file needing to be manipulated
fin="Campus_Met_Data_Student.csv"
# Strips the associate date and time from the csv file
date_parser=lambda x: pd.datetime.strptime(x,"%d/%m/%Y %H:%M")
#obs=pd.read_csv(fin,parse_dates=["TIMESTAMP"],date_parser=date_parser,index_col=0)
obs=pd.read_csv(fin,parse_dates=True,index_col=0)
# assign obs resample to the mean of the column d
obs=obs.resample("D").mean()
# reads the head of the columns in the csv
obs.head(50)

# auto_regress using only air temperature and relative humdidity as the candidate 
# predictor variables; 
pred,r2 = tom.auto_regress(obs["AirTC_Avg"],obs[["AirTC_Avg","RH"]],2019,1,0.05,True)

# have to run the original variable due to an issue reading the csv file
pred

# assigns the subplot for the line graph
fig,ax=plt.subplots(1,1)
# plots the sim and obs values, assigns different colors, and assigns a label for the legend
ax.plot(pred["sim"],color="black",label="SIM")
ax.plot(pred["obs"],color="red",alpha=0.5,label="OBS")
# creates the legend
ax.legend()
# autoformat the dates given
fig.autofmt_xdate()
# labels the x and y axis of the plot
ax.set_xlabel("2019 data")
ax.set_ylabel("Temperature (deg C)")

# takes the variables mean and finds the mean and mean absolute error for the original model
# prints both the me and mae
me_sin=np.mean(pred["sim"]-pred["obs"]) 
print("Mean error is: ", me_sin)
mae_sin=np.mean(np.abs(pred["sim"]-pred["obs"])) 
print("Mean absolute error is: ", mae_sin)

#me_sim=np.mean(pred["clim"]-pred["obs"]) 
#print("Mean error is: ", me_sim)
#mae_sim=np.mean(np.abs(pred["clim"]-pred["obs"])) 
#print("Mean absolute error is: ", mae_sim)

# takes the variables mean and finds the mean and mean absolute error for the new model
# prints both the me and mae
me_sim=np.mean(pred["sim"]-pred["clim"]) 
print("Mean error is: ", me_sim)
mae_sim=np.mean(np.abs(pred["sim"]-pred["clim"])) 
print("Mean absolute error is: ", mae_sim)

# creates the ss variable to find the skill score on what model is more accurate to use
SS=(1-mae_sin/mae_sim)
# prints the ss 
print(SS)

