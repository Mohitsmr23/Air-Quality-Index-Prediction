# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Importing the dataset
dataset = pd.read_csv('Data.csv')

#Feature selection
dataset=dataset.drop(columns=["TM","Tm","VM"])

#handling the missing data
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy="mean")
dataset=imputer.fit_transform(dataset)
imputer=SimpleImputer(missing_values=0,strategy="mean")

dataset=imputer.fit_transform(dataset)

dataset=pd.DataFrame(dataset)

corrmat = dataset.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(16,15))

#plot heat map
g=sns.heatmap(dataset[top_corr_features].corr(),annot=True,cmap="RdYlGn")

sns.pairplot(dataset)


X = dataset.iloc[:, 0:-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)


# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
regressor = Sequential()

# Adding the input layer and the first hidden layer
regressor.add(Dense(output_dim = 128, kernel_initializer='normal', activation = 'relu', input_dim = X_train.shape[1]))

# Adding the second hidden layer
regressor.add(Dense(output_dim = 256, kernel_initializer='normal', activation = 'relu'))

#classifier.add(Dense(output_dim = 17, init = 'uniform', activation = 'relu'))

regressor.add(Dense(output_dim = 256, kernel_initializer='normal', activation = 'relu'))

# Adding the output layer
regressor.add(Dense(output_dim = 1, kernel_initializer='normal', activation = 'linear'))

# Compiling the ANN
regressor.compile(optimizer = 'adam', loss = 'mean_absolute_error', metrics = ['mean_absolute_error'])
#adam is the algorithm for stochastic gradient descent

# Fitting the ANN to the Training set
regressor.fit(X_train, y_train, batch_size = 100, nb_epoch = 5000)
regressor.summary()

#predicting the test set 
y_pred = regressor.predict(X_test)   


history = regressor.fit(X_train, y_train, epochs=2000, batch_size=100)

#plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Mean absolute error')
plt.xlabel('Epoch')
plt.plot(history.history['mean_absolute_error'])

# Plot training & validation loss values

plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.plot(history.history['loss'])
plt.legend(['Train','Test'],loc='upper left')
plt.show()

 
