import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x=np.array([[1,3],[1,2],[1,1.5],[1.5,2],[2,3],[2.5,1.5],[2,1],[3,1],[3,2],[3.5,1],[3.5,3]])
y=6*[0]+[1]*5
X,Y=np.mgrid[0:4:200j,0:3:100j]
print(X.shape)
print(Y)
