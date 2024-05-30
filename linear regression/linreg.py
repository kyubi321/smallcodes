# import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import regressor
from sklearn import datasets
from sklearn.model_selection import train_test_split



class linear_regression:
    def __init__(self, lr=0.01, iter=1000):
        self.lr = lr
        self.iter = iter
        self.bias = None
        self.weight = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # now we are setting the value of weight for each n_feature to be zero
        self.weight = np.zeros(n_features)
        self.bias = 0

        # now we have to iterate the following code to the max iteration we provided
        for _ in range(self.iter):

        # calculate y_pred
            ypred = np.dot(X, self.weight) + self.bias

        # now we need to calculate the weights and bias
            dw = (1 / n_samples) * np.dot(X.T, (ypred-y))
            db = (1 / n_samples) * np.sum(ypred - y)

        # now we update the weights using the equation
            self.weight = self.weight - self.lr * dw
        # now we update the bias using the equation
            self.bias = self.bias - self.lr * db

    def predict(self, X):
        # now we predict using the new updated values
        y_pred = np.dot(X, self.weight) + self.bias
        return y_pred

X, y = datasets.make_regression(n_samples=100,n_features=1, noise=20,random_state=4)
X_train , X_test , Y_train, Y_test = train_test_split(X,y ,test_size=0.25,random_state=1234)
#fig = plt.figure(figsize=(8,6))
#plt.scatter(X[:,0] ,y, color="b",marker= 'o',s =30)
#plt.show()

reg = linear_regression()
reg.fit(X_train,Y_train)
prediction = reg.predict((X_test))

y_pred_line = reg.predict(X)
fig = plt.figure(figsize=(8,6))
m1 = plt.scatter(X_train,Y_train,cmap="viridis",s =10)
m2 = plt.scatter(X_test,Y_test,cmap="viridis",s =10)
plt.plot(X,y_pred_line,color = "black",linewidth = 2,label ="prediction")
plt.show()