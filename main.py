import numpy as np
import pandas as pd

from sklearn import neighbors , metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('car.data')



X=data[[
    'buying',
    'maint',
    'safety']].values

Y=data[['class']]



#converting data by label encoder
Le=LabelEncoder()
for i in range(len(X[0])):
    X[:,i]=Le.fit_transform(X[:,i])




#for y
label_mapping={
    'unacc':0,
    'acc':1,
    'good':2,
    'vgood':3
}

Y['class']=Y['class'].map(label_mapping)

y=np.array(Y)



#create model

knn=neighbors.KNeighborsClassifier(n_neighbors=25, weights="uniform")

#train model
X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.2)

knn.fit(X_train,Y_train)

predictions=knn.predict(X_test)

accuracy=metrics.accuracy_score(Y_test, predictions)
print("predictions:", predictions)
print('accuracy:', accuracy)

a=175

print("actual value:", Y.loc[a][0])
print("predicted value:", knn.predict(X)[a])