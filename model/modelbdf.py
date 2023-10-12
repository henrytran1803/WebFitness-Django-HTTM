import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from joblib import dump
from sklearn import linear_model
from sklearn.model_selection import train_test_split
df = pd.read_csv('bodyfat.csv', low_memory=False)
X = df.drop('BodyFat', axis=1)
y = df['BodyFat']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model =linear_model.LinearRegression()
model.fit(X, y)

# score = model.score(X_test, y_test)
#
# print("R-squared score:", score)
# from sklearn.metrics import r2_score
#
# # Dự đoán kết quả trên tập test
# y_pred = model.predict(X_test)
#
# # Tính R-squared
# r2 = r2_score(y_test, y_pred)*100
#
# print("R-squared: {:.2f}".format(r2))


# Lưu mô hình vào một tệp
dump(model, 'linear_regression_model.joblib')
