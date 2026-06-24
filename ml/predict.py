from pathlib import Path

import joblib
import pandas as pd

script_dir = Path(__file__).parent
model_path = script_dir / "student_rf.pkl"
feature_columns_path = script_dir / "feature_columns.pkl"
loaded_object = joblib.load(model_path)
feature_columns = joblib.load(feature_columns_path)

student_data = {
        "study_hours_per_day": 3,
        "deep_work_sessions": 2,
        "assignment_completion_rate": 80,
        "attendance_percentage": 90,
        "social_media_hours": 2,
        "doomscrolling_before_sleep": 1,
        "ai_tool_usage_hours": 1,
        "gaming_hours": 1,
        "stress_level": 4,
        "motivation_level": 4,
        "focus_score": 7,
        "procrastination_index": 2,
        "mental_state": 'Distracted',
        "sleep_hours": 7,
        "caffeine_intake": 1,
        "physical_activity_hours": 1,
        "internet_quality": 4,
        "financial_stress": 2,
        "learning_style": 'Visual',
        "productivity_after_midnight": 3,
        "revision_efficiency": 4,
        "burnout_risk": 2,
        "consistency_score": 3
}

prediction_input = pd.DataFrame([student_data])
prediction_input = pd.get_dummies(prediction_input, drop_first=True)
prediction_input = prediction_input.reindex(
    columns=feature_columns,
    fill_value=0
)
##print(f"Prediction input columns: {prediction_input.columns.tolist()}")
#print(prediction_input.shape)
#print(len(feature_columns))

prediction = loaded_object.predict(prediction_input)
print(f"Predicted final exam score: {prediction[0]:.2f}")

