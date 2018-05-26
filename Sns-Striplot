#用来求不同类别的成员分布
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data1 = pd.read_excel('/Users/marcowang/Downloads/Distirbution.xlsx')
print(data1.head())
print(type(data1))
data1.region.astype('category')
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
sns.stripplot(x= 'region', y='total', data=data1, size = 3, jitter=True)
plt.title('Score Distritution by Region')
fig.savefig('Score Distritution by Region', dpi=100)
plt.show()
