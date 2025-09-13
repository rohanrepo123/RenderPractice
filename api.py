import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import OrdinalEncoder
# from sklearn
df = pd.read_csv('bank-additional-full.csv',sep=';') # adding error_bad_lines=False to skip problematic lines

df[df['age']> 85].dropna()
df.drop(columns=['poutcome'],inplace=True)
ordinal_encoder = OrdinalEncoder()
df['job'] = ordinal_encoder.fit_transform(df[['job']])
df['marital'] = ordinal_encoder.fit_transform(df[['marital']])
df['default'] = ordinal_encoder.fit_transform(df[['default']])
df['education'] = ordinal_encoder.fit_transform(df[['education']])
df['contact'] = ordinal_encoder.fit_transform(df[['contact']])
df['pdays'] = ordinal_encoder.fit_transform(df[['pdays']])
df['housing'] = ordinal_encoder.fit_transform(df[['housing']])
df['loan'] = ordinal_encoder.fit_transform(df[['loan']])
df['month'] = ordinal_encoder.fit_transform(df[['month']])
df['day_of_week'] = ordinal_encoder.fit_transform(df[['day_of_week']])
df['y']=(df['y']=="yes").astype(int)

train , validate ,test = np.split(df.sample(frac=1), [int(0.7*len(df)), int(0.8*len(df))])
def data(dataframe,oversample=False ):
  x = (dataframe[dataframe.columns[:-1]]).values
  y =((dataframe[dataframe.columns[-1]]).values)
  st = StandardScaler()
  x= st.fit_transform(x)
  if oversample:
      x , y  = RandomOverSampler().fit_resample(x,y)
  data = np.hstack((x,np.reshape(y,(-1,1))))
  return data,x,y
train , x_train, y_train = data(train,oversample=True)
validate , x_validate, y_validate = data(validate,oversample=False)
test , x_test, y_test = data(test,oversample=False)

len(train[train == 0])   # it is now numpy array
len(train[train == 1])   # it is now numpy array


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
knn = KNeighborsClassifier(n_neighbors=3)
knn_model = knn.fit(x_train,y_train)
y_predict = knn_model.predict(x_test)
print(classification_report(y_test,y_predict))