import pandas as pd
from joblib import dump
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


# Chọn mô hình Random Forest và sử dụng các tham số đã chỉ định
model_rf = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    min_samples_split=10,
    min_samples_leaf=1,
    random_state=42
)
model_rf.fit(X, y)
dump(model_rf, 'RandomForestRegressor.joblib')

print("Model trained and saved successfully!")
