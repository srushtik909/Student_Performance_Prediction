import os
import pickle
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

# ✅ Sample Data (Fixed Syntax & Equal Length Lists)
data = {
    "student_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "study_time": [10, 15, 8, 20, 25, 5, 30, 12, 18, 22],
    "absences": [2, 5, 0, 7, 3, 10, 1, 4, 6, 2],
    "past_scores": [75, 80, 65, 90, 85, 60, 95, 78, 82, 88],
    "Online_Courses_Completed": [2, 1, 0, 3, 4, 2, 5, 3, 1, 2],
    "Assignment_Completion_Rate": [100, 71, 60, 63, 59, 63, 91, 88, 52, 100],
    "Self_Reported_Stress_Level": ["High", "Medium", "Low", "Low", "Medium", "High", "Low", "Low", "Low", "Medium"],
    "Time_Spent_on_Social_Media": [15, 12, 20, 8, 5, 25, 30, 10, 14, 18],
    "gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "school_type": ["Public", "Private", "Public", "Private", "Public", "Private", "Public", "Private", "Public", "Private"],
    "final_score": [78, 85, 70, 92, 88, 65, 98, 80, 84, 90]
}

df = pd.DataFrame(data)

# ✅ Define Features and Target (Removing 'student_id')
X = df.drop(columns=["final_score", "student_id"])
y = df["final_score"]

# ✅ Preprocessing
categorical_features = ["gender", "school_type", "Self_Reported_Stress_Level"]
numerical_features = ["study_time", "absences", "past_scores", "Online_Courses_Completed", "Assignment_Completion_Rate", "Time_Spent_on_Social_Media"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numerical_features),
    ("cat", OneHotEncoder(), categorical_features)
])

# ✅ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train Model
rf_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

rf_pipeline.fit(X_train, y_train)

# ✅ Create directory if not exists
model_dir = "models"
os.makedirs(model_dir, exist_ok=True)

# ✅ Save Model
with open(os.path.join(model_dir, "rf_model.pkl"), "wb") as file:
    pickle.dump(rf_pipeline, file)

print("✅ Model trained and saved successfully in 'models/' folder.")
