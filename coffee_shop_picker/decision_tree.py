from sklearn import tree
from . import dataset
import copy

data = dataset.Dataset('data.csv')
X = copy.deepcopy(data.inputs)
Y = copy.deepcopy(data.labels)
#print(X)
#print(Y)
clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)
#default
prediction = clf.predict([[150, 1, 1, 4.5, 2]])

def predict(budget, hasWifi, environment, quality, noise):
    prediction = clf.predict([[budget, hasWifi, environment, quality, noise]])
    return prediction
