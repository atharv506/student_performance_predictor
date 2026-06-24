from pathlib import Path
import math

import pandas as pd

project_root = Path(__file__).resolve().parent.parent
dataset_path = project_root / "data" / "student_performance_dataset.csv"

df = pd.read_csv(dataset_path)

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib


script_dir = Path(__file__).parent

X = df[[
    "study_hours_per_day",
    "deep_work_sessions",
    "assignment_completion_rate",
    "attendance_percentage",
    "social_media_hours",
    "doomscrolling_before_sleep",
    "ai_tool_usage_hours",
    "gaming_hours",
    "stress_level",
    "motivation_level",
    "focus_score",
    "procrastination_index",
    "mental_state",    
    "sleep_hours",
    "caffeine_intake",
    "physical_activity_hours",
    "internet_quality", 
    "financial_stress",
    "learning_style",   
    "productivity_after_midnight",
    "revision_efficiency",
    "burnout_risk",
    "consistency_score"
]]

X = pd.get_dummies(X, drop_first=True)
#print(X.columns.tolist())
joblib.dump(X.columns.tolist(), script_dir / "feature_columns.pkl")#save the feature columns to a file for later use in prediction
y = df["final_exam_score"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=700, random_state=42, max_depth=12, min_samples_split=10, min_samples_leaf=2)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
##rmse = math.sqrt(mean_squared_error(y_test, y_pred))
##r2 = r2_score(y_test, y_pred)
##
##print(f"RMSE: {rmse:.2f}")
##print(f"R2: {r2:.2f}")

model_path = script_dir / "student_rf.pkl"

joblib.dump(model, model_path)