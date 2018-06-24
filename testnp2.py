import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn import linear_model
diabetes=datasets.load_diabetes()
a=diabetes.data
b=diabetes.target
x_train=a[:422]
y_train=b[:422]
x_test=a[-20:]
y_test=b[-20:]
linreg=linear_model.LinearRegression()
linreg.fit(x_train,y_train)
predict=linreg.predict(x_test)
s=linreg.score(x_test,y_test)
print(predict,"\n",y_test,"\n",s)
