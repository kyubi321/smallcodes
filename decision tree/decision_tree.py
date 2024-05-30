import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn import tree

dataset = pd.read_csv("bill_authentication.csv")
dataset.shape
dataset.head()

X = dataset.drop('Class', axis=1)
y = dataset['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

classifier = DecisionTreeClassifier(criterion='gini',max_depth=3,random_state=0)

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print('Model accuracy score with criterion gini index: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

y_pred_gini_train = classifier.predict(X_train)
print(y_pred_gini_train)


print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_gini_train)))
print('Training set score: {:.4f}'.format(classifier.score(X_train, y_train)))
print('Test set score: {:.4f}'.format(classifier.score(X_test, y_test)))
print("\n")
# Plotting the tree
plt.figure(figsize=(12, 8))
plot_tree(classifier, filled=True, feature_names=X.columns, class_names=['0', '1'])
plt.title('Decision Tree - Gini Index')
plt.show()

clf_ig = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
clf_ig.fit(X_train, y_train)
y_pred_ig = clf_ig.predict(X_test)
print('Model accuracy score with criterion IG: {0:0.4f}'. format(accuracy_score(y_test, y_pred_ig)))
y_pred_train_ig = clf_ig.predict(X_train)
print(y_pred_train_ig)
print('Training-set accuracy score: {0:0.4f}'. format(accuracy_score(y_train, y_pred_train_ig)))
print('Training set score: {:.4f}'.format(clf_ig.score(X_train, y_train)))
print('Test set score: {:.4f}'.format(clf_ig.score(X_test, y_test)))
# Plotting the tree
plt.figure(figsize=(12, 8))
plot_tree(clf_ig, filled=True, feature_names=X.columns, class_names=['0', '1'])
plt.title('Decision Tree - Information Gain (Entropy)')
plt.show()