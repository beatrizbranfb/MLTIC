import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import os 

df = pd.read_excel("Módulo 2/Wine/wineDB.xlsx")


#heatmap = sb.heatmap(df.corr())

#heatmap.get_figure().savefig("mapaVinho.png")

#print(df.columns)

x_columns = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']

y_columns = ['quality']

x = df[x_columns]
y = df[y_columns]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 101)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)

#print(lr.coef_)

preds = lr.predict(x_test)
print(preds)

plt.xlabel("valores esperados")
plt.ylabel("valores preditos")
linear = plt.scatter(y_test, preds)

linear.get_figure().savefig("RegressaoLinear.png")