# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:26:41 2022

@author: oby_pc
"""
import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


#upload data
data=pd.read_csv("Life_Expectancy_Data.csv")

#data preprocessing
data2=data.fillna(data.mean())  #handling nan values

# catogorical to numeric
from sklearn import preprocessing


dummies = pd.get_dummies(data2.Status) #dummy varaible for status
data3=pd.concat([data2, dummies], axis='columns')#Concatenate the dummies to original dataframe
data3=data3.drop(['Status', 'Developing'], axis='columns')
 
"""
because of there is lots of country and fewer country data, it is non sense to make
countries numerical. It will of course raise the accurucy but when we do train test split
probably there is no test data for each country. 
so i merged countries and year each other 

"""
# dummies = pd.get_dummies(data2.Country)
# data3=pd.concat([data3, dummies], axis='columns')#Concatenate the dummies to original dataframe
# data3=data3.drop(['Country'], axis='columns')

life_expectancy=data2.iloc[:,3]
y=life_expectancy
Y=y.values
x=data3.iloc[:,4:]
X=x.values

#extrack some information in data
print("mean of global life expactancy is: %.2f" %life_expectancy.mean())


#corolation between values
coralation_matrix=data2.corr()
coralation_matrix2=data2.corr()['Life expectancy '].sort_values()
"""
coomment about coralation- in theese matrix it can be said that,
Schooling,Income composition of resources, BMI has direct coralation,
moreover, Adult Mortality and HIV/AIDS has negative coralation.
"""

#statistics of data
byCountry=data3.groupby("Country").mean() 
byCountry2=data3.groupby("Country").describe() 

#life expectancy vs features plots
for i in range(19):
    x_value=byCountry.iloc[:,1]
    y_value=byCountry.iloc[:,i+2]    
    plt.figure(i)
    plt.title("life Expectancy vs {}".format(byCountry.columns[i+2]))
    plt.xlabel("Life Expectancy") 
    plt.ylabel(byCountry.columns[i+2])
    plt.scatter(x_value,y_value)
    plt.show()
"""
about above figures it can be inferred that
1-there is an inverse ratio between the adult mortality and life expactancy.
2-there is not linear corelation between expenditure on health. On the other hand
when percentage of expenditure obove 1500's, life expectancy rises proportionaly (dramatic increase)
3-Higher palio inmune makes life expantacy higher
4-diphttheria and life expactancy rises accordingly
5-HIV deaths drastically lower life expectancy 
6-above 10000 GDP increases life expactancy
7-thinness certainly has the effect of lowering life expectancy
8-there is direct corelation both income and schooling between life expactancy

"""
#histogram plots
for i in range(19):
    x_value=byCountry.iloc[:,i+2]    
    plt.figure(i)
    plt.title("Histogram of {}".format(byCountry.columns[i+2]))
    his= plt.hist(x_value)    
    plt.show()


#test train split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.33,random_state=0)


#model built for multilinear regression

from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(x_train, y_train)
y_pred= lin_reg.predict(x_test)


print('multilinear R2 value is:')
print(r2_score(y_test, lin_reg.predict(x_test)))




# backward elemination,
import statsmodels.api as sm
X=np.append(arr=np.ones((2938,1)).astype(int), values=x, axis=1) #beta değeri belirlemek için veri başına 1 ler ekledik
X_l=x.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]].values
X_l=np.array(X_l, dtype=float)
model = sm.OLS(y,X_l).fit()
print(model.summary())


#remove the features p value higher than 0.05 which
X_l=x.iloc[:,[0,3,4,5,6,7,8,9,10,13,14,15,16,17]].values
X_l=np.array(X_l, dtype=float)
model = sm.OLS(y,X_l).fit()
print(model.summary())





#build new model for relevant features
x1=x.iloc[:,[0,3,4,5,6,7,8,9,10,13,14,15,16,17]].values
x_train, x_test, y_train, y_test=train_test_split(x1,y,test_size=0.33,random_state=0)
lin_reg2=LinearRegression()
lin_reg2.fit(x_train, y_train)
y_pred= lin_reg2.predict(x_test)


print('model2 multilinear R2 value is:')
print(r2_score(y_test, lin_reg2.predict(x_test))) #no much succes improvement

#remove the features p value higher than 0 which
X_l=x.iloc[:,[0,3,5,6,7,8,9,10,13,14,15,16,17]].values
X_l=np.array(X_l, dtype=float)
model = sm.OLS(y,X_l).fit()
print(model.summary())

#build new model for relevant features
x2=x.iloc[:,[0,3,5,6,7,8,9,10,13,14,15,16,17]]
x_train, x_test, y_train, y_test=train_test_split(x2,y,test_size=0.33,random_state=0)
lin_reg3=LinearRegression()
lin_reg3.fit(x_train, y_train)
y_pred= lin_reg3.predict(x_test)

print('model3 multilinear R2 value is:')
print(r2_score(y, lin_reg3.predict(x2))) #our score get lower.



#polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)

print('degree 2 Polynomial R2 value')
print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X)))) #interesting result. our score get bigger



poly_reg = PolynomialFeatures(degree = 3)
x_poly = poly_reg.fit_transform(X)
lin_reg3 = LinearRegression()
lin_reg3.fit(x_poly,y)

print('degree 3 Polynomial R2 value')
print(r2_score(Y, lin_reg3.predict(poly_reg.fit_transform(X)))) #very bad score.



# scaling data

from sklearn.preprocessing import StandardScaler

sc1=StandardScaler()

x_scaled = sc1.fit_transform(X)

sc2=StandardScaler()
y_scaled = np.ravel(sc2.fit_transform(Y.reshape(-1,1)))


# SVR model
from sklearn.svm import SVR
x_train, x_test, y_train, y_test=train_test_split(x_scaled,y_scaled,test_size=0.33,random_state=0)

svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_train,y_train)

print('SVR R2 value')
print(r2_score(y_test, svr_reg.predict(x_test))) #0.88 very good result



#Decision Tree

from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)

r_dt.fit(x_train,y_train)
print('Decision Tree R2 value')
print(r2_score(y_test, r_dt.predict(x_test))) 





#Random Forest Regression
from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators = 10,random_state=0)
rf_reg.fit(x_train,y_train.ravel())


print('Random Forest value')
print(r2_score(y_test, rf_reg.predict(x_test))) #0.937 best score


# random forest with unscaled data
x_train, x_test, y_train, y_test=train_test_split(X,Y,test_size=0.33,random_state=0)

rf_reg=RandomForestRegressor(n_estimators = 10,random_state=0)
rf_reg.fit(x_train,y_train.ravel())


print('Random Forest value')
print(r2_score(y_test, rf_reg.predict(x_test))) #0.938 still best score


"""
result:
    we get best result with random forest regression model which is 0.93.
    
    
"""















