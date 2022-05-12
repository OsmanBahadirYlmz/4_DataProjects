#libraries

import numpy as np
import pandas as pd


df=pd.read_csv('MobilePhones.csv')


x = df.iloc[:,0:20].values #bağımsız değişkenler
y = df.iloc[:,20:].values #bağımlı değişken


from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)

x = df.iloc[:,0:20].values #independent variables
y = df.iloc[:,20:].values #dependent variable


from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=0)


from sklearn.preprocessing import StandardScaler

sc=StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)




from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


from sklearn.svm import SVC
svc = SVC(kernel='linear')
svc.fit(X_train, np.ravel(y_train))

y_pred = svc.predict(X_test)
cm = confusion_matrix(y_test,y_pred)


print('SVC ')
print(cm)
print("\n accuracy:", accuracy_score(y_test, y_pred))
print("model score",svc.score(X_test,y_test))






