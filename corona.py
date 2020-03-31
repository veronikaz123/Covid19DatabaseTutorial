import pandas as pd
#url = 'https://raw.githubusercontent.com/hxchua/datadoubleconfirm/master/datasets/arrivals2018.csv'

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
df = pd.read_csv(url, error_bad_lines=False)

print(df.head())
