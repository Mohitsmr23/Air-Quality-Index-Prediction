#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams


# In[5]:


pwd


# In[6]:


df = pd.read_csv(r'C:\\Users\\mohit\\data.txt')

df.sample(5)


# In[7]:


print("df.shape : ", df.shape)


# In[8]:


print(df.columns)


# In[9]:


df.info()


# In[10]:


df[df['PM 2.5'].isnull()]


# In[11]:


df.fillna(method='ffill', inplace = True)


# In[12]:



rcParams['figure.figsize'] = 11.7,8.27

sns.lineplot(data = df["PM 2.5"], color="red", label="PM2.5")
plt.title('Visualising PM2.5 Data')
plt.show()


# In[13]:


duplicateRowsDF = df[df.duplicated()]
 
print("Duplicate Rows except first occurrence based on all columns are :")
print(duplicateRowsDF)


# In[14]:


df = df[df.duplicated() == False]

print(df.shape)


# In[15]:


df.info()


# In[16]:


df.describe().T


# In[17]:


sns.lineplot(data = df["PM 2.5"], color="orange", label="PM2.5 (No Duplicates)")
plt.title('Visualising the PM2.5 Data (with No Duplicates)')
plt.show()


# In[18]:


pm_ = list(df['PM 2.5'])

Acceptable = []

for pm in pm_:
    if pm >= 151:
        Acceptable.append(0)
    else:
        Acceptable.append(1)

df['Acceptable'] = Acceptable

df.sample(3)


# In[19]:


rcParams['figure.figsize'] = 4.75,4.75

print(df.Acceptable.value_counts())

sns.countplot(y = "Acceptable", data = df, palette = 'winter_r')
plt.show()


# In[20]:


cols =  list(df.columns)

plt.figure(figsize=(20, 20))

for i in range(1, 9):
    plt.subplot(3, 4, i)
    sns.scatterplot(x = cols[i - 1], y = df['PM 2.5'],data = df, hue = "Acceptable", palette = "husl")


# In[21]:


corrmat = df.corr()
top_corr_features = corrmat.index[:-1] # dropping 'Acceptable'

plt.figure(figsize=(7,7))

#plot heat map
sns.heatmap(df[top_corr_features].corr(),annot = True, linewidths=.5)
# print(corrmat)
plt.show()


# In[124]:


df=df.drop(columns=['Acceptable'])
sns.pairplot(df)


# In[111]:


from sklearn.model_selection import train_test_split

X = df[[ 'T','TM','Tm','SLP', 'H', 'VV','VM','V']]
y = df['PM 2.5']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10, random_state = 45)


# In[112]:


print('Length of X_train', len(X_train))
print('Length of X_test', len(X_test))
print('Length of y_train', len(y_train))
print('Length of y_test', len(y_test))


# In[113]:


from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

print("lr.score : ", lr.score(X_test, y_test))
print("lr.coef_ : ",lr.coef_)
print("lr.intercept_ : ",lr.intercept_)


# In[114]:


print("lr.score of training data: ", lr.score(X_train, y_train))


# In[115]:


from sklearn.model_selection import cross_val_score
score = cross_val_score(lr , X, y, cv = 5)

print(score)
print("Mean score : ",score.mean())


# In[116]:


coeff_df = pd.DataFrame(lr.coef_, X.columns, columns = ['Coefficient'])
coeff_df


# In[117]:


from sklearn import metrics

prediction = lr.predict(X_test)

print('MAE:', metrics.mean_absolute_error(y_test, prediction))
print('MSE:', metrics.mean_squared_error(y_test, prediction))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))


# In[118]:


print("Prediction Values:",prediction)


# In[119]:



plt.scatter(y_test,prediction)
plt.show()
    
 


# In[120]:


plt.title("Prediction and actual value Comparison")
plt.plot(prediction)
plt.ylabel('y_test[i],pediction[i]')
plt.xlabel('i')
plt.plot(y_test)
plt.legend(['Prediction','Actual'],loc='upper left')
plt.show()


# In[ ]:





# In[ ]:




