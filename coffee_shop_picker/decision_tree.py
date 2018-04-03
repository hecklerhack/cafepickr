from sklearn import tree

X = [[150, 0, 0, 1.5, 1],
[120, 0, 0, 3.0, 1],
[130, 0, 0, 4.0, 1],
[140, 0, 2, 3.5, 1],
[155, 0, 0, 4.5, 2],
[140, 0, 0, 4.5, 1],
[140, 0, 0, 3.5, 1],
[140, 0, 2, 2.0, 0],
[135, 0, 0, 3.0, 0],
[140, 0, 0, 2.0, 2],
[120, 1, 1, 3.0, 2],
[95, 1, 1, 3.0, 2],
[120, 1, 2, 3.0, 0],
[120, 1, 2, 4.5, 2],
[120, 1, 1, 4.5, 1],
[140, 0, 1, 3.5, 1],
[140, 0, 2, 3.5, 1],
[150, 1, 1, 3.5, 1],
[140, 0, 1, 4.0, 2],
[125, 0, 0, 4.5, 2],
[100, 0, 0, 4.5, 2]]

Y = ['kivhan',
'kivhan',
'kivhan',
'kivhan',
'kivhan',
'kivhan',
'kivhan',
'kivhan',
'kivhan',
'kivhan',
'bos',
'bos',
'bos',
'bos',
'bos',
'seattles',
'seattles',
'seattles',
'gloriajeans',
'gloriajeans',
'gloriajeans']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)
#default
prediction = clf.predict([[150, 1, 1, 4.5, 2]])

def predict(budget, hasWifi, environment, quality, noise):
    prediction = clf.predict([[budget, hasWifi, environment, quality, noise]])
    return prediction
