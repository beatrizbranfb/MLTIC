import seaborn as sb
import pandas as pd

titanic = pd.read_csv('titanic.csv', quotechar='"', sep=';')
titanic.head()


titanic.survived.value_counts()
titanic.embark_town.value_counts()

heatmap = sb.heatmap(titanic.isnull()) 

figura = heatmap.get_figure().savefig("heatmap.png")

titanic.loc[titanic.female == 0] & (titanic.who == 'woman') | (titanic.female == 1 & (titanic.who == 'man'))