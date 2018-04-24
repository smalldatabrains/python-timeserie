import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from autocorrelation import autocorrelate
from scipy.fftpack import fft
from scipy import signal

os.chdir('/home/eric/Desktop/smalldatabrains/website/python-timeserie/')

#load data
data=pd.read_csv('LD2011_2014.txt',sep=";")
print(data.shape)

#first column is the timestamp
#every other column represent a customer

#convert data to proper types
data.iloc[:,0]=pd.to_datetime(data.iloc[:,0])
data.iloc[:,1]=pd.to_numeric(data.iloc[:,1].str.replace(',','.'))
# for column in range(1,data.shape[1]-1):
# 	print("column",column,"is being processed")
# 	data.iloc[:,column]=pd.to_numeric(data.iloc[:,column].str.replace(',','.'))

#client1 prestudy
client1=data.iloc[:,0:2]
client1.columns=['timestamp','consumption']
client1.head()


client1=client1.set_index('timestamp')
#resampling
client1_daily=client1.resample('D').mean()

#ploting values
plt.plot(client1_daily)
plt.show()

#signal decomposition
signal=client1_daily.dropna().consumption
N=len(signal)
t = np.linspace(0, N,N)
sin=np.sin(2*np.pi*t)


#mean, rms, energy and power of a signal
mean=sum(signal)/len(signal)
rms=np.sqrt(np.dot(signal,signal)/len(signal))
energy=np.dot(signal,signal)
power=energy/len(signal)



#autocorrelation
acr=autocorrelate(signal)


#spectrum of the signal
y_fft=fft(client1_flat)
plt.plot(np.abs(y_fft))

#intercorrelation : to find a given pattern in a signal

#stationarity of time serie

#signal smoothing


#rolling statistics


#trend and seasonality


#estimating & eliminating trend


#moving window


#estimating & eliminating seasonality


#forecasting ARIMA


#forecasting LSTM

