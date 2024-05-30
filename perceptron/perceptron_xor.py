# import necessary modules
from sklearn.neural_network import MLPClassifier
import numpy as np
import matplotlib.pyplot as plt

# provide the training data for the model
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,1,1,0])

# create an classifier model
p = MLPClassifier(max_iter=1000)

# train the model
p.fit(X,y)

# provide testing data
tst_exp = np.array([[0,0],[0,1],[1,0],[1,1]])

# getting the output predicted by the model
predicted = p.predict(tst_exp)

print("test_sample  , output_predicted\n")
for i in range(len(tst_exp)):
    print(f"     {tst_exp[i]}  ,  {predicted[i]}")

plt.scatter(tst_exp[:, 0] ,tst_exp[:, 1] , c=predicted ,cmap="viridis" ,marker="v" ,s =100)
plt.title("perceptron xor")
plt.xlabel("x_values")
plt.ylabel("y_values")
plt.grid(True)
plt.show()

