import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

data = pd.read_excel('/Users/marcowang/Downloads/Distirbution.xlsx')
print(data.head())
df = data.loc[:,['region','total']]
print(df.head())

szx = df[df.region == 'SZX'].total
sao = df[df.region == 'SAO'].total
cao = df[df.region == 'CAO'].total
nao = df[df.region == 'NAO'].total
jso = df[df.region == 'JSO'].total
szo = df[df.region == 'SZO'].total
dzo = df[df.region == 'DZO'].total
nlo = df[df.region == 'NLO'].total
pto = df[df.region == 'PTO'].total
sho = df[df.region == 'SHO'].total
nah = df[df.region == 'NAH'].total
mzo = df[df.region == 'MZO'].total

szx1 = szx[szx<1500]
sao1 = sao[sao<1500]
cao1 = cao[cao<1500]
nao1 = nao[nao<1500]
jso1 = jso[jso<1500]
szo1 = szo[szo<1500]
dzo1 = dzo[dzo<1500]
nlo1 = nlo[nlo<1500]
pto1 = pto[pto<1500]
sho1 = sho[sho<1500]
nah1 = nah[nah<1500]
mzo1 = mzo[mzo<1500]





cho = [szo,sao,cao,nao,jso,szo,dzo,nlo,pto,sho,nah,mzo]

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y

# Compute ECDFs
x_szx, y_szx = ecdf(szx1)
x_sao, y_sao = ecdf(sao1)
x_cao, y_cao = ecdf(cao1)
x_nao, y_nao = ecdf(nao1)
x_jso, y_jso = ecdf(jso1)
x_szo, y_szo = ecdf(szo1)
x_dzo, y_dzo = ecdf(dzo1)
x_nlo, y_nlo = ecdf(nlo1)
x_pto, y_pto = ecdf(pto1)
x_sho, y_sho = ecdf(sho1)
x_nah, y_nah = ecdf(nah1)
x_mzo, y_mzo = ecdf(mzo1)

# Plot all ECDFs on the same plot
plt.plot(x_szx, y_szx,marker = '.', linestyle = 'none')
plt.plot(x_sao, y_sao,marker = '.', linestyle = 'none')
plt.plot(x_cao, y_cao,marker = '.', linestyle = 'none')
plt.plot(x_nao, y_nao,marker = '.', linestyle = 'none')
plt.plot(x_jso, y_jso,marker = '.', linestyle = 'none')
plt.plot(x_szo, y_szo,marker = '.', linestyle = 'none')
plt.plot(x_dzo, y_dzo,marker = '.', linestyle = 'none')
plt.plot(x_nlo, y_nlo,marker = '.', linestyle = 'none')
plt.plot(x_pto, y_pto,marker = '.', linestyle = 'none')
plt.plot(x_sho, y_sho,marker = '.', linestyle = 'none')
plt.plot(x_nah, y_nah,marker = '.', linestyle = 'none')
plt.plot(x_mzo, y_mzo,marker = '.', linestyle = 'none')

# Make nice margins
plt.margins(0.02)
fig = plt.gcf()
fig.set_size_inches(20.5, 10.5)
# Annotate the plot
plt.legend(('szo','sao','cao','nao','jso','szo','dzo','nlo','pto','sho','nah','mzo'), loc='center')
_ = plt.xlabel('Medals')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
