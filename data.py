import pandas  as pd 
import numpy as np 
df = pd.read_csv('Admission_Predict.csv')
# import joblib

# model = joblib.load("model.pkl")


df = df.drop(columns=['Serial No.'])

from sklearn.model_selection import train_test_split
x = df.iloc[:,0:-1]
y = df.iloc[:,-1]

from sklearn.preprocessing import StandardScaler
st = StandardScaler()
x = st.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
model = lr.fit(x_train,y_train)

# x = model.predict(x_test)

# print(x)
