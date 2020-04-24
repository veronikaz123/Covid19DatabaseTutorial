import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
from datetime import date
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'

df = pd.read_csv(url, error_bad_lines=False)

#print(df.head(100))
country = input("giv et landenavn:  ") or "Denmark"
country = df.loc[df['Country/Region']==country].index
country = country[len(country)-1]

data = df.to_numpy()
head = df.columns.to_numpy()
lande = data[:,1]
data = data[:,4:]
dage = np.array(range(0,len(data[0,:])))
head = head[4:]

def func(x,a,b):
  return b*a**x

def lin(x,a,b):
    return a*x+b

xData = np.extract(data[country,:]>2,dage[:]).astype(int)
yData = np.extract(data[country,:]>2,data[country,:]).astype(int)
dates = np.extract(data[country,:]>2,head[:])
print(yData)

popt, pcov = curve_fit(func,xData[:len(xData)-1],yData[:len(xData)-1],[1.3,0.5])

xData = [pd.to_datetime(d) for d in dates]
min = yData[0]
max = yData[len(yData)-1]
plt.text(xData[0],max-100,'T: {:.4f}'.format(np.log(2)/np.log(popt[0])) , fontsize=12)
plt.text(xData[0],(max-min)/2,'a: {:.4f}'.format(popt[0]) , fontsize=12)
plt.text(xData[0],min+100, 'max: {:d}'.format(yData[len(yData)-1]), fontsize=12)


plt.plot(xData,func(np.extract(data[country,:]>2,dage[:]).astype(int),*popt),'r-')
plt.scatter(xData,yData)
#plt.yscale('log')
plt.xticks(rotation=20)
plt.grid()
plt.show()
