import pandas as pd
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
df = pd.read_csv('exercise.csv', low_memory=False)
exercise_labels = []
for index, row in df.iterrows():
    exercise_type = row['ExerciseType']
    exercise_difficulty = row['DifficultyLevel']
    label = int((exercise_type - 1) * 3 + exercise_difficulty)
    exercise_labels.append(label)
df['label'] = exercise_labels
# Suy ngược type và difficulty từ label
# exercise_type = (label - 1) // 3 + 1
# exercise_difficulty = (label - 1) % 3 + 1
X = df[['BMI', 'BodyFatPercentage', 'Weight', 'Height','TDEE']]
y = df['label']  # Label là cột bạn muốn dự đoán
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model_rf = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    min_samples_split=10,
    min_samples_leaf=1,
    random_state=42
)
model_rf.fit(X, y)

score = model_rf.score(X_test, y_test)

print("R-squared score:", score)
from sklearn.metrics import r2_score

# Dự đoán kết quả trên tập test
y_pred = model_rf.predict(X_test)

# Tính R-squared
r2 = r2_score(y_test, y_pred)*100

print("R-squared: {:.2f}".format(r2))
# dump(model_rf, 'RandomForestRegressor.joblib')
#
# print("Model trained and saved successfully!")
