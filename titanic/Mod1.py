import seaborn as sb
import pandas as pd

titanic = pd.read_csv('titanic/titanic.csv', quotechar='"', sep=';')
titanic.head()


titanic.survived.value_counts()
titanic.embark_town.value_counts()

heatmap = sb.heatmap(titanic.isnull()) 

figura = heatmap.get_figure().savefig("heatmap.png")

#titanic.loc[titanic.female == 0] & (titanic.who == 'woman') | (titanic.female == 1 & (titanic.who == 'man'))

#iris dataset ->

iris = pd.read_csv('titanic/iris.csv', quotechar='"', sep=';')
iris.head()
iris.species.value_counts()
valores = iris.describe()

#print(iris.columns)
#print(titanic.columns)

#valores_titanic = titanic.describe()
#print(valores_titanic)

#existe = "female" in titanic.columns
#print(existe)

