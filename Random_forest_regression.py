
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv('Data.csv')

#Feature selection
dataset=dataset.drop(columns=["TM","Tm","VM"])

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy="mean",)
dataset=imputer.fit_transform(dataset)

dataset=pd.DataFrame(dataset)
X= dataset.iloc[:, 0:-1].values
y= dataset.iloc[:, -1].values



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)


from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=1000,random_state=0)
regressor.fit(X_train,y_train)


y_pred=regressor.predict(X_test)

from sklearn.metrics import mean_absolute_error 
mean_absolute_error(y_test,y_pred) 

plt.title("Prediction and actual value comparision")
plt.plot(y_pred)
plt.plot(y_test)
plt.ylabel('y_pred[i], y_test[i]')
plt.xlabel('i')
plt.legend(['Actual','Prediction'],loc='upper left')
plt.show()


#for every value on x axis, avg of outcomes of n random trees is calculated.
#on increasing number of trees, total steps dont increase much as no of splits dont increase how many trees we take.