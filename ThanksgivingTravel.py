

# Importing Data
import pandas as pd
from datetime import datetime, timedelta
from scipy.stats import ttest_rel

df = pd.read_csv('nationalonly.csv', encoding='utf-8')

# filtering and removing unnecessary columns and creating new columns for use
# df = df[df['Level']=='National']
# df.dropna(axis=1, how='any',inplace=True)
date_format = '%Y/%m/%d'
df['Date'] = [datetime.strptime(date, date_format) for date in df['Date']]
df['Year'] = [date.year for date in  df['Date']]
df['Month']  = [date.month for date in df['Date']]
df['Day'] = [date.day for date in df['Date']]

# # creating dates for thanksgiving in the past 3 years
tk_2019_date = datetime.strptime('2019/11/28', date_format)
tk_2020_date = datetime.strptime('2020/11/26', date_format)
tk_2021_date = datetime.strptime('2021/11/25',date_format)

# separating data into years
data_2019 = df[df['Year']==2019]
data_2020 = df[df['Year']==2020]
data_2021 = df[df['Year']==2021]

# filtering to specifically only week before thanksgiving
begin_2019 = tk_2019_date - timedelta(days=19)
end_2019 = tk_2019_date - timedelta(days=12)
data_2019 = data_2019[(data_2019['Date']> begin_2019) & (data_2019['Date']<= end_2019)]

begin_2020 = tk_2020_date - timedelta(days=19)
end_2020 = tk_2020_date - timedelta(days=12)
data_2020 = data_2020[(data_2020['Date']> begin_2020) & (data_2020['Date']<= end_2020)]

begin_2021 = tk_2021_date - timedelta(days=19)
end_2021 = tk_2021_date - timedelta(days=12)
data_2021 = data_2021[(data_2021['Date']> begin_2021) & (data_2021['Date'] <= end_2021)]

# weighing different years
"""
population in 2019 was 331,028,075 (U.S. Census Bureau)
population in 2020 was 332,013,802 (U.S. Census Bureau)
population in 2021 is 332,952,379 (U.S. Census Bureau)
"""
weight_2019 = round(331028075/332952379, 3)
weight_2020 = round(332013802/332952379, 3)
weight_2021 = round(332952379/332952379, 3)





#Creating Arrays for total trips each year
trips2019 = np.array(data_2019['Number of Trips'])
trips2020 = np.array(data_2020['Number of Trips'])
trips2021 = np.array(data_2021['Number of Trips'])

#Creating Arrays for total trips each year group >= 5 & < 50 miles

Med_trips_2019 = []
Med_trips_2020 = []
Med_trips_2021 = []

dframe = [data_2019,data_2020,data_2021]
appendto = [Med_trips_2019,Med_trips_2020,Med_trips_2021]
weight = [weight_2019,weight_2020,weight_2021]
for d,a,w in zip(dframe,appendto,weight):
    for i,j,k,l in zip(d['Number of Trips 5-10'],d['Number of Trips 10-25'],d['Number of Trips 25-50'],d['Number of Trips 50-100']):
        sum_of_Med = (i + j + k + l) * w
        a.append(sum_of_Med)

#Creating Arrays for total trips each year group >= 100

Long_trips_2019 = []
Long_trips_2020 = []
Long_trips_2021 = []


appendto = [Long_trips_2019,Long_trips_2020,Long_trips_2021]
for d,a,w in zip(dframe,appendto,weight):
    for i,j,k in zip(d['Number of Trips 100-250'],d['Number of Trips 250-500'],d['Number of Trips >=500']):
        sum_of_Long = (i + j + k) * w
        a.append(sum_of_Long)
    




#Comparing Total Trips
Total_2019n2020 = ttest_rel(trips2019,trips2020).pvalue
Total_2020n2021 = ttest_rel(trips2020,trips2021).pvalue
Total_2019n2021 = ttest_rel(trips2019,trips2021).pvalue
print('Total Trips 19to20:  ',Total_2019n2020)
print('Total Trips 20to21:  ',Total_2020n2021)
print('Total Trips 19to21:  ',Total_2019n2021)




#Comparing Med Trips
Med_2019n2020 = ttest_rel(Med_trips_2019,Med_trips_2020).pvalue
Med_2020n2021 = ttest_rel(Med_trips_2020,Med_trips_2021).pvalue
Med_2019n2021 = ttest_rel(Med_trips_2019,Med_trips_2021).pvalue
print('Med Trips 19to20:  ',Med_2019n2020)
print('Med Trips 20to21:  ',Med_2020n2021)
print('Med Trips 19to21:  ',Med_2019n2021)




#Comparing Long Trips
Long_2019n2020 = ttest_rel(Long_trips_2019,Long_trips_2020).pvalue
Long_2020n2021 = ttest_rel(Long_trips_2020,Long_trips_2021).pvalue
Long_2019n2021 = ttest_rel(Long_trips_2019,Long_trips_2021).pvalue
print('Long Trips 19to20:  ',Long_2019n2020)
print('Long Trips 20to21:  ',Long_2020n2021)
print('Long Trips 19to21:  ',Long_2019n2021)







