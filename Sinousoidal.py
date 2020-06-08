# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:53:46 2019

@author: natel
"""
# assigning the plot limitations
ig,ax=plt.subplots(1,1)
# assigning the observed values as the color black and label it yearly temp
ax.plot(doy_clim["obs"],color="black", label = "Yearly Temp")

# assigning the observed values as the color yellow and label it sin curve
# this is the basic sin curve that follow natural law
ax.plot(doy_clim["clim"],color="yellow",alpha= 7, label = "Sin curve")
# adding a legend
ax.legend()
# the x axis is going to auto format to the current dates
fig.autofmt_xdate()
# the x axis will be labeled by the dates 2016-2019
ax.set_xlabel("2016-2019 dates")
# the y axis is going to be labeled for the temperature in C
ax.set_ylabel("Temperature (deg C)")
