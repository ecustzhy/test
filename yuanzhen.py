import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
data=pd.read_excel('datacollect20180112.xlsx','Sheet3',skiprows=3,header=None)
data.columns=['i','time','x1','x2','x3','x4','x5','y1','y2','y']
x=data[['x1','x2','x3','x4','x5']]
y=data['y']
#print(y)
#sns.pairplot(data,x_vars=['x1','x2','x3','x4','x5'],y_vars='y',size=7,aspect=0.8)
#plt.show()
#c=np.random.permutation(len(x))
x1=np.array(x)[:4000]
y1=np.array(y)[:4000]
linreg=linear_model.LinearRegression()
linreg.fit(x1,y1)
y_predict=linreg.predict(x1)
a=linreg.coef_
b=linreg.intercept_
c=linreg.score(x1,y1)
print(a,b,c)


