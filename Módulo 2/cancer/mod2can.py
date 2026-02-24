import pandas as pd
import seaborn as sb

df = pd.read_csv("Módulo 2/cancer/cancer_data.csv", on_bad_lines='skip')
 
print(df.columns)

x_columns = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean' , 'smoothness_mean' , 'compactness_mean' , 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean' , 'radius_se;texture_se', 'perimeter_se', 'area_se', 'smoothness_se' , 'compactness_se' , 'concavity_se' ,'concave points_se', 'symmetry_se' , 'fractal_dimension_se' , 'radius_worst' , 'texture_worst' , 'perimeter_worst' , 'area_worst','smoothness_worst','compactness_worst','concavity_worst']
y_columns = ['diagnosis']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=101)
x_train.shape

from sklearn.metrics import accuracy_score, SVC

model = SVC()

preds = model.predict(x_test)
print(accuracy_score(y_test, preds))