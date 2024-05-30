# we import the necessary modules that to be used
from sklearn.linear_model import Perceptron
import numpy as np
import matplotlib.pyplot as plt

# we provide the train data i.e the And gate values x are the input and y are the output
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

# now we call our perceptron model object with max iteration for training.
p = Perceptron(max_iter=1000)

# now we train our data using fit method
p.fit(X,y)

# now we need to test our model
# provide test sample
test_sample = np.array([[0,0],[0,1],[1,0],[1,1]])

# using predict function
predicted = p.predict(test_sample)

print("test_sample , output_predicted\n")
for i in range(len(test_sample)):
    print(f"     {test_sample[i]}  ,  {predicted[i]}")


plt.scatter( test_sample[:,0] ,test_sample[:,1],c=predicted , cmap="viridis" , marker="o",s=200)
plt.xlabel("x_input")
plt.title("perceptron And")
plt.ylabel("y_input")
plt.show()



