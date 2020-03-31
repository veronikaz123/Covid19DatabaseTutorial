import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
from datetime import date
print('running')

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

df = pd.read_csv(url, error_bad_lines=False)
#df.set_index('Country/Region',inplace=True)


df.loc[df['Country/Region']=='Italy']
print(df.loc[df['Province/State']=='Denmark'])

data = df.to_numpy()
head = df.columns.to_numpy()
lande = data[:,1]
dage = np.array(range(4,len(data[0,:])))
data = data[:,4:]

country = df.loc[df['Country/Region']=='Denmark'].index
country = country[2]

def func2(x,a,b):
#  return a*np.exp(b*x)
  return b*a**x

xData = np.extract(data[country,:]>800,dage[:]).astype(int)
yData = np.extract(data[country,:]>800,data[170,:]).astype(int)

popt, pcov = curve_fit(func2,xData,yData,[1.3,0.5])
scenarie2 = popt
#print('T: ', np.log(2)/np.log(popt[0]))
#plt.text(45,1200,np.log(2)/np.log(popt[0]) , fontsize=12)
#plt.text(43,1200,'T2: ', fontsize=12)
plt.text(42,1100,'a_scenarie2: ', fontsize=12)
plt.text(48,1100,popt[0],fontsize=12)

yData = np.extract(data[country,:]>2,data[170,:]).astype(int)
yData = np.extract(yData<800,yData).astype(int)

xData = np.extract(data[country,:]>2,dage[:]).astype(int)
xData = np.extract(yData<800,xData).astype(int)


popt, pcov = curve_fit(func2,xData,yData,[1.3,0.5])

scenarie1 = popt
print('T: ',np.log(2)/np.log(popt[0]))

plt.plot(range(42,66),func2(range(42,66),*scenarie2),'r-')
plt.plot(xData,func2(xData,*scenarie1),'r-')

xData = np.extract(data[country,:]>2,dage[:])
yData = np.extract(data[country,:]>2,data[170,:])

#plt.text(43,1400,'T1:' , fontsize=12)
#plt.text(45,1400,np.log(2)/np.log(popt[0]) , fontsize=12)
plt.text(42,1400,'a_scenarie1:' , fontsize=12)
plt.text(48,1400,popt[0], fontsize=12)
plt.scatter(xData,yData)
plt.grid()
plt.show()
