import pandas as pd
import numpy as np
data1 = pd.read_excel('/Volumes/PNY Hook/手游for Alex/5.4-5.10 summary-33604409.xlsx')
print(data1.head())
data2 = pd.read_excel('/Volumes/PNY Hook/手游for Alex/5.11-5.16-summary-31955750.xlsx')
data3 = pd.read_excel('/Volumes/PNY Hook/手游for Alex/5.17-5.21 summary-17283343.xlsx')
#data1 = pd.ExcelFile('/Volumes/PNY Hook/手游for Alex/5.4-5.10 summary-33604409.xlsx')
#data2 = pd.ExcelFile('/Volumes/PNY Hook/手游for Alex/5.11-5.16-summary-31955750.xlsx')
#data3 = pd.ExcelFile('/Volumes/PNY Hook/手游for Alex/5.17-5.21 summary-17283343.xlsx')
print(data1.sheet_names)
print(data2.sheet_names)
print(data3.sheet_names)


df1 = data1.parse('Sheet1')
df2 = data2.parse('5.11-5.16')
df3 = data3.parse('Sheet1')
#df4 = datat.parse('用户活跃度4')
df = pd.concat([df1,df2,df3],axis = 0)
df.index = df['开始时间']
out_csv = 'data.csv'
df.to_csv(out_csv)
dataC = pd.read_csv('/Users/marcowang/data.csv',parse_dates = True, index_col = '开始时间')

dataC['count'] = 1
print(dataC.head())


active_rate = dataC.loc[:,['关卡','count']]
print(active_rate.head())
print(type(active_rate))
daily = active_rate.resample('H').sum()
print(daily)
out_csv = 'dataC.csv'
daily.to_csv(out_csv)
import matplotlib.pyplot as plt

daily.plot(title = 'Active Rate per Hour',kind = 'bar')
plt.ylabel('Amount')
plt.xlabel('Time')
plt.grid(True)
a = list(daily.index)
plt.yticks = a
plt.show()
