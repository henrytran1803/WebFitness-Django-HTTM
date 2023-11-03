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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
score = linear_model.score(X_test, y_test)

print("R-squared score:", score)
from sklearn.metrics import r2_score

# Dự đoán kết quả trên tập test
y_pred = linear_model.predict(X_test)

# Tính R-squared
r2 = r2_score(y_test, y_pred)*100

print("R-squared: {:.2f}".format(r2))
#
# dump(linear_model, 'linear_regression_model_bdf.joblib')
#
# print("Model trained and saved successfully!")

