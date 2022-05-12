# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:16:44 2021

@author: oby_pc
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
df=pd.read_csv("winequality.csv")



# from pandas.plotting import scatter_matrix
# scatter_matrix(df.iloc[:,:2])


# # ikili ilişkilere grafikle bakmak için for döngüsü .corr un grafiksel hali

# for x in range (12):
#     plt.figure(x)
#     plt.scatter(X_scaled2["quality"],X_scaled2.iloc[:,x],s=1)
#     plt.title(X_scaled2.columns[x])




# #cluster yapma   
# from sklearn.cluster import KMeans
# KM=KMeans(n_clusters=3)

# KM.fit(X_scaled[:,0:2])
# y_pred=KM.predict(X_scaled[:,0:2])


# plt.scatter(X_scaled[:,0],X_scaled[:,1], c=y_pred)
# a=KM.cluster_centers_   
# # plt.scatter(KM.cluster_centers_[:,0],KM.cluster_centers_[:,1], c=[0,1,2], s=550,marker="*",edgecolors="b")

"""
#inert bularak kaç cluster olacağını hesaplama
inert=[]

for i in range (10):
 
    KM2=KMeans(n_clusters=(i+1))
    KM2.fit(X_scaled[:,0:2])
    inert.append(KM2.inertia_)

plt.figure(13) #yukarıda 12 plot çizildiği için
plt.plot(inert)
"""


#1.Veri önişleme
x=df.iloc[:,1:11].values
y=df.iloc[:,11:].values


from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)


from sklearn.preprocessing import StandardScaler
scale= StandardScaler()

X_train=scale.fit_transform(x_train)
X_test=scale.fit_transform(x_test)

# X_scaled2=pd.DataFrame(X_scaled, columns=df.columns) #colon ismi yazsın istiyorsak

#model oluşturma

#miltireg
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train, y_train)
y_pred_lin= regressor.predict(X_test)

from sklearn.metrics import r2_score
print('Linear R2 degeri')
print(r2_score(y_test, y_pred_lin))

plt.scatter(y_test,y_pred_lin)

import statsmodels.api as sm
X=np.append(arr=np.ones((14,1)).astype(int), values=sonveriler, axis=1)
X_l=sonveriler.iloc[:,[0,1,2,3,4,5]].values
X_l=np.array(X_l, dtype=float)
model = sm.OLS(sonveriler.iloc[:,-1:],X_l).fit()
print(model.summary())

#svm
from sklearn.svm import SVR
svc_reg=SVR(kernel="rbf")
svc_reg.fit(X_train,y_train)
y_pred_svc=svc_reg.predict(x_test)
plt.scatter(y_test, y_pred_svc)