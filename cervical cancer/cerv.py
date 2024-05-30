import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from sklearn import metrics
dataset = pd.read_csv("kag_risk_factors_cervical_cancer.csv")
#print(dataset.head())
#print(dataset.describe())
X = dataset.drop("Biopsy",axis=1)
Y = dataset["Biopsy"]

x_train,x_test,y_train,y_test = train_test_split(X,Y, random_state=24, test_size=0.25)
clf = SVC(kernel='linear')
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)
acc = metrics.accuracy_score(y_test,y_pred)
print(acc)