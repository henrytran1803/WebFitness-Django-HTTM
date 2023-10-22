import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from joblib import dump

df = pd.read_csv("bodyfat.csv")

bin_labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

df['BodyFatEncoded'] = pd.cut(df['BodyFat'], bins=21, labels=bin_labels)

X = df.drop(columns=['BodyFat', 'Density'])

y = df['BodyFat']

linear_model = LinearRegression()
linear_model.fit(X, y)


dump(linear_model, 'linear_regression_model_bdf.joblib')

print("Model trained and saved successfully!")

