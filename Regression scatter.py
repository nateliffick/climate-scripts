# -*- coding: utf-8 -*-
"""


"""
# Import modules
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import tom

# assigns a variable to the csv file
fin="Campus_Met_Data_Student.csv"
# strips the date and time from the csv file
date_parser=lambda x: pd.datetime.strptime(x,"%d/%m/%Y %H:%M")
#obs=pd.read_csv(fin,parse_dates=["TIMESTAMP"],date_parser=date_parser,index_col=0)
obs=pd.read_csv(fin,parse_dates=True,index_col=0)
# resample the means 
obs=obs.resample("D").mean()
# prints all the column heading in the csv
obs.head(50)

# states all the variables in the csv and formates the specific columns subjected to autoregression
pred,r2 = tom.auto_regress(obs["AirTC_Avg"],obs[["AirTC_Avg","RH"]],2019,1,0.05,True)

# prints the pred variable which is included in the csv file
pred

# creates a plot
fig,ax=plt.subplots(1,1)
# creates a scatter plot for observed values and simulated values
ax.scatter(pred["obs"],pred["sim"],s=1)
# sets the scatter plots x and y axis limits
ax.set_xlim([-5,26])
ax.set_ylim([-5,26])
# sets the scatter plot x and y labels
ax.set_xlabel("Observed Air Temperature (deg C)")
ax.set_ylabel("Modeled Air Temperature (deg C)")
# assigns grid lines to the x and y axis
ax.yaxis.grid()
ax.xaxis.grid()
# arranges the scatter plot points between the values -5 and 27
x=np.arange(-5,27)
# assigns the scatter plot points as black 
ax.plot(x,x,color='black')




