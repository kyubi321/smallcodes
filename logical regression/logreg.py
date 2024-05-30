
# import necessary packages
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

class Logistic_regression:

     def __init__(self,lr = 0.00001, itera = 1000):
         self.lr = lr
         self.itera = itera
         self.weights = None
         self.bias = None

     def fit(self,X,y):
         n_samples , n_features = X.shape
         # now we have to set the weights to be zero for all the features

         self.weights = np.zeros(n_features)
         # now we set the bias to be zero
         self.bias = 0

         for _ in range(self.itera):
             linear_pred = np.dot(X,self.weights)+ self.bias
             ypred = 1/(1+np.exp(-linear_pred))

             dw = (1/n_samples) *np.dot(X.T, (ypred-y))
             db = (1/n_samples) * np.sum(ypred-y)

             self.weights = self.weights - self.lr *dw
             self.bias = self.bias - self.lr *db

     def predict(self,X):
         linear_pred = np.dot(X, self.weights) + self.bias
         y_pred = 1 / (1 + np.exp(-linear_pred))
         # for every value in y_pred if it is greater than the 0.5 then assign 0
         # else assign 1
         class_pred = [0 if y<=0.5 else 1 for y in y_pred]
         return class_pred


bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target
Xtrain, Xtest ,ytrain, ytest = train_test_split(X,y, test_size=0.25 , random_state=1234)


# create an instance of the class
reg = Logistic_regression()
# fit the data with our new dataset
reg.fit(Xtrain,ytrain)
# make prediction using our model
prediction = reg.predict(Xtest)
def accur(y_pred ,ytest):
    return np.sum(y_pred == ytest)/len(ytest)

acc = accur(prediction, ytest)
print(acc)



