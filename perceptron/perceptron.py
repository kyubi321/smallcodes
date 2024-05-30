import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the breast cancer dataset
data = load_breast_cancer()
x = data.data
y = data.target

# Display feature names and target values
#print(data.feature_names)
#print(y)

# Create a DataFrame for better visualization
df = pd.DataFrame(data=data.data, columns=data.feature_names)
#print(df.head())

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Display training and testing sets
#print(x_train)
#print("%%%%%%%%%%%%%")
#print(x_test)
#print("%%%%%%%%%%%%%")
#print(y_train)
#print("%%%%%%%%%%%%%")
#print(y_test)
#print("%%%%%%%%%%%%%")

# Create and train a Perceptron model
clf = Perceptron(max_iter=1000)
clf.fit(x_train, y_train)

# Make predictions on the testing set
ypred = clf.predict(x_test)
print("Predictions:", ypred)

# Calculate and display accuracy
acc = accuracy_score(y_test, ypred)
print("Accuracy:", acc)

# Generate and display the confusion matrix
conf_matrix = confusion_matrix(y_test, ypred)
print("Confusion Matrix:")
print(conf_matrix)



