
#libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score

#importing data
df=pd.read_csv('diamonds.csv')

#data preprocessing------------------------
#missing values

print(df.info())
#There is 6 missing values in carat and 3 in price. 
#Since there are not much missing values we can drop them
df=df.dropna()

#outier analysis
import seaborn as sns
sns.boxplot(df['price'])

#The graph clearly shows that values greater than 2*e10 are extreame values.
#filter theese valuese
df2=df[df["price"]<2*(10**10)]
sns.boxplot(df2['price'])

#now it can be seen in graph that above 12500 can be seen as 
#ouier but all of is bigger in carat so i want to keep them
#i wont use df3 but maybe for test
df3=df[df["price"]<12500]
sns.boxplot(df3['price'])

#encoding catagorical to numeric

from sklearn import preprocessing

dummies = pd.get_dummies(df2.cut) #get dummies cut column
df2 = pd.concat([df2, dummies], axis='columns')
df2=df2.drop(['cut'], axis='columns') #remove dummy variable


dummies = pd.get_dummies(df2.color) #get dummies cut column
df2 = pd.concat([df2, dummies], axis='columns')
df2=df2.drop(['color'], axis='columns') #remove dummy variable


dummies = pd.get_dummies(df2.clarity) #get dummies cut column
df2 = pd.concat([df2, dummies], axis='columns')
df2=df2.drop(['clarity'], axis='columns') #remove dummy variable

y=df2.iloc[:,1:2]
x=df2.drop(['price'], axis='columns')
Y = y.values
X = x.values


#Test train split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(X,Y,test_size=0.33,random_state=0)



# #Model Building-----------------

# 1- multilinear Regression
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train, y_train)
y_pred= regressor.predict(x_test)
Y_pred= regressor.predict(X)

#calculating score r2 score

from sklearn.metrics import r2_score

print('Linear regression R2 value :')
print(r2_score(Y, regressor.predict(X)))

#calculating RMSE score
import math
 
MSE = np.square(np.subtract(y_test,y_pred)).mean() 
 
RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE)




# # 2-polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)


print('2nd degree Polynomial regression R2 value')
print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))

y_pred=lin_reg2.predict(poly_reg.fit_transform(x_test))
MSE = np.square(np.subtract(y_test,y_pred)).mean()  
RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE)

#--with train test split
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(x_train)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y_train)


print('2nd degree Polynomial regression R2 value')
print(r2_score(y_test, lin_reg2.predict(poly_reg.fit_transform(x_test))))

y_pred=lin_reg2.predict(poly_reg.fit_transform(x_test))
MSE = np.square(np.subtract(y_test,y_pred)).mean()  
RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE)


# #3 rd degree 

poly_reg = PolynomialFeatures(degree = 3)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)

print('3rd degree Polynomial regression R2 value')
print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X))))

y_pred=lin_reg2.predict(poly_reg.fit_transform(x_test))

MSE = np.square(np.subtract(y_test,y_pred)).mean() 
 
RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE)

#3rd degree only test
poly_reg = PolynomialFeatures(degree = 3)
x_poly = poly_reg.fit_transform(x_train)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y_train)


print('3nd degree Polynomial regression R2 value')
print(r2_score(y_test, lin_reg2.predict(poly_reg.fit_transform(x_test))))

y_pred=lin_reg2.predict(poly_reg.fit_transform(x_test))
MSE = np.square(np.subtract(y_test,y_pred)).mean()  
RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE)

#4 th degree
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x_train)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y_train)


print('2nd degree Polynomial regression R2 value')
print(r2_score(y_test, lin_reg2.predict(poly_reg.fit_transform(x_test))))

y_pred=lin_reg2.predict(poly_reg.fit_transform(x_test))
MSE = np.square(np.subtract(y_test,y_pred)).mean()  
RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE)





#3-SVR model
#for svr we need to scale our data
from sklearn.preprocessing import StandardScaler

sc1=StandardScaler()

x_scaled = sc1.fit_transform(X)

sc2=StandardScaler()
y_scaled = np.ravel(sc2.fit_transform(Y.reshape(-1,1)))


from sklearn.svm import SVR

svr_reg = SVR(kernel='rbf')
svr_reg.fit(x_scaled,y_scaled)

print('SVR R2 value')
print(r2_score(y_scaled, svr_reg.predict(x_scaled)))

y_pred=svr_reg.predict(x_test)

MSE = np.square(np.subtract(y_test,y_pred)).mean() 
 
RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE)

# #4- Decision Tree Regression
# from sklearn.tree import DecisionTreeRegressor
# r_dt = DecisionTreeRegressor(random_state=0)
# r_dt.fit(X,Y)
# Y_pred=r_dt.predict(X)

# print('Decision Tree R2 value:')
# print(r2_score(Y, r_dt.predict(X)))



# #Since score is very high Decision Tree maybe over fitting
# #test for over fitting
# x_train, x_test, y_train, y_test=train_test_split(X,Y,test_size=0.33,random_state=0)

# r_dt2 = DecisionTreeRegressor(random_state=0)
# r_dt2.fit(x_train,y_train)
# y_pred=r_dt2.predict(x_test)
# print('Decision Tree R2 value with only test inputs:')
# print(r2_score(y_test, r_dt2.predict(x_test)))

# #it is not overfitting probably decision tree is the best model

# MSE = np.square(np.subtract(y_test,y_pred)).mean() 
 
# RMSE = math.sqrt(MSE)
# print("Root Mean Square Error:\n")
# print(RMSE) #5632.562077376492



#5-Random forest Regression
from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators = 10,random_state=0)
rf_reg.fit(x_train,y_train.ravel())

print('Random Forest R2 value:')
print(r2_score(Y, rf_reg.predict(X)))

print('Random Forest R2 value with only test input:')
print(r2_score(y_test, rf_reg.predict(x_test)))

Y_pred=rf_reg.predict(X)

#memory error so i will try only y_test values
# MSE = np.square(np.subtract(Y,Y_pred)).mean()  
# RMSE = math.sqrt(MSE)
# print("Root Mean Square Error:\n")
# print(RMSE)


y_pred=rf_reg.predict(x_test)

MSE = np.square(np.subtract(y_test,y_pred)).mean()  
RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE) #5620.557780016719



"""
#----------RESULT-----------
#best model is 2 degree polynomial regression which has RMSE=752 and r2=0.96
#in order to improve nalyse results


"""
#rewrite our model again
# poly_reg = PolynomialFeatures(degree = 2)
# x_poly = poly_reg.fit_transform(x_train)
# lin_reg2 = LinearRegression()
# lin_reg2.fit(x_poly,y_train)


# print('2nd degree Polynomial regression R2 value')
# print(r2_score(y_test, lin_reg2.predict(poly_reg.fit_transform(x_test))))

# y_pred=lin_reg2.predict(poly_reg.fit_transform(x_test))
# MSE = np.square(np.subtract(y_test,y_pred)).mean()  
# RMSE = math.sqrt(MSE)
# print("Root Mean Square Error:\n")
# print(RMSE)

#lets look at which predictions are has higher error


# error=abs(y_test-y_pred)
# result=np.concatenate((y_test,y_pred,error),axis=1)
# resultSorted=pd.DataFrame(result.copy())


#we can see the above big errors accurs when the price is above 12500
#it is because of theese valuese are very high when comparing the rest
#lest filter them and try again


# #preprocessing
df3=df[df["price"]<12500]

dummies = pd.get_dummies(df3.cut) #get dummies cut column
df3 = pd.concat([df3, dummies], axis='columns')
df3=df3.drop(['cut'], axis='columns') #remove dummy variable


dummies = pd.get_dummies(df3.color) #get dummies cut column
df3 = pd.concat([df3, dummies], axis='columns')
df3=df3.drop(['color'], axis='columns') #remove dummy variable


dummies = pd.get_dummies(df3.clarity) #get dummies cut column
df3 = pd.concat([df3, dummies], axis='columns')
df3=df3.drop(['clarity'], axis='columns') #remove dummy variable

y=df3.iloc[:,1:2]
x=df3.drop(['price'], axis='columns')
Y = y.values
X = x.values

#test train split
x_train, x_test, y_train, y_test=train_test_split(X,Y,test_size=0.33,random_state=0)

#model 
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(x_train)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y_train)


print('2nd degree Polynomial regression R2 value for price lower than 12500')
print(r2_score(y_test, lin_reg2.predict(poly_reg.fit_transform(x_test))))

y_pred=lin_reg2.predict(poly_reg.fit_transform(x_test))
MSE = np.square(np.subtract(y_test,y_pred)).mean()  
RMSE = math.sqrt(MSE)
print("Root Mean Square Error:\n")
print(RMSE)

error=abs(y_test-y_pred)
result=np.concatenate((y_test,y_pred,error),axis=1)
resultSorted=pd.DataFrame(result.copy())

# """
# 2nd degree Polynomial regression R2 value for price lower than 12500
# 0.9630889413845781
# Root Mean Square Error:
# 554.4370735473415

# there is a improvement but still maka big error in higher values.

# """



from sklearn.tree import DecisionTreeRegressor
r_dt2 = DecisionTreeRegressor(random_state=0)
r_dt2.fit(x_train,y_train)
y_pred=r_dt2.predict(x_test)
print('Decision Tree R2 value with only test inputs:')
print(r2_score(y_test, r_dt2.predict(x_test)))

#it is not overfitting probably decision tree is the best model

error=np.zeros(15538)

sum=0
for i in range(15538):
    error[i]=abs(y_test[i]-y_pred[i])
    error=np.square(y_test[i]-y_pred[i])
    sum+=error

# import math

# RMSE= math.sqrt(sum/15538)  
# print(RMSE) 









