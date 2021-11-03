import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style


doc = pd.read_csv("vgsales.csv")

doc = doc[['Rank', 'Global_Sales']]

predict = "Global_Sales"

x = np.array(doc.drop([predict], 1))
y = np.array(doc[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.001)

# linear = linear_model.LinearRegression()

# linear.fit(x_train, y_train)
# with open("linear.pickle", "wb") as f:
#     pickle.dump(linear, f)

pickle_in = open("linear.pickle", "rb")
linear = pickle.load(pickle_in)
# acc = linear.score(x_test, y_test)
# print(acc*100)

print("coefficient: ", linear.coef_)
print("intercept: ", linear.intercept_)

predictions = linear.predict(x_test)

for i in range(len(predictions)):
    print(predictions[i]*10, x_test[i], y_test[i]*10)

p = 'Rank'
style.use("ggplot")
pyplot.scatter(doc[p], doc['Global_Sales'])
pyplot.xlabel(p)
pyplot.ylabel("Global_Sales")
pyplot.show()