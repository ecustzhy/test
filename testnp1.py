import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
iris=datasets.load_iris()
a=iris.data
b=iris.target
c=np.random.permutation(150)
x_train=a[c[:-10]]
y_train=b[c[:-10]]
x_test=a[c[-10:]]
y_test=b[c[-10:]]
knn=KNeighborsClassifier()
knn.fit(x_train,y_train)
r=knn.predict(x_test)
print(iris)

