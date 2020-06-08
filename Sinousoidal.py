# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:53:46 2019

@author: natel
"""

ig,ax=plt.subplots(1,1)
ax.plot(doy_clim["obs"],color="black", label = "Yearly Temp")

ax.plot(doy_clim["clim"],color="yellow",alpha= 7, label = "Sin curve")
ax.legend()
fig.autofmt_xdate()
ax.set_xlabel("2016-2019 dates")
ax.set_ylabel("Temperature (deg C)")