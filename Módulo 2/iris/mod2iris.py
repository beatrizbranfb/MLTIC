import pandas as pd
import seaborn as sb

df = pd.read_csv("Módulo 2/iris/iris2.csv")  

#print(df.head)

sb.pairplot(df, hue="species")

