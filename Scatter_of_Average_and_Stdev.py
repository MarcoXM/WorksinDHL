import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data= pd.read_excel('/Users/marcowang/Downloads/result.xlsx')
print(data.head())
data1 = pd.ExcelFile('/Users/marcowang/Downloads/result.xlsx')
df = data1.parse('Sheet3')
print(data1.sheet_names)
print(type(data))
print(type(data1))
print(data['区域'])
print(data[['区域']])
x = list(data['标准差'])
y = list(data['平均数'])
size = data['人数']
name = list(data['区域'])
plt.scatter(x,y, s =size, c = np.random.rand(16))
plt.xlabel('Standard Deviation')
plt.ylabel('Average')
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)

b = np.linspace(0, 400, 400)
a = 0.7*b
d = np.linspace(0, 400, 400)
c = 0.43661971830985913*d
plt.plot(b,a,linestyle="-.",)
plt.plot(d,c,)

plt.annotate('Average/STd = 0.7', xy=(300, 210), xytext=(230, 250),
            arrowprops=dict(facecolor='green', shrink=0.05),)
plt.annotate('Whole Country Level ', xy=(350, 150), xytext=(280, 80),
            arrowprops=dict(facecolor='red', shrink=0.05),)

plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
plt.title('Result of Mobile Game')
n=0
for X,Y in zip(x,y):
   
    plt.text(X+0.3, Y+15, name[n], ha='center', va= 'bottom')
    n += 1
fig.savefig('test2png.png', dpi=100)
plt.show()
