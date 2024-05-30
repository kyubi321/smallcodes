import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import load_wine

dataset = load_wine()
print(dataset)
X = pd.DataFrame(dataset.data,columns=dataset.feature_names)
y = pd.Series(dataset.target , name='quality')
X_train,Y_train,X_test,Y_test  = 