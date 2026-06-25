from pathlib import Path

import joblib
import pandas as pd

script_dir = Path(__file__).parent
model_path = script_dir / "student_rf.pkl"
feature_columns_path = script_dir / "feature_columns.pkl"
loaded_object = joblib.load(model_path)
feature_columns = joblib.load(feature_columns_path)

student_data = {
        "study_hours_per_day": 2.1,
        "deep_work_sessions": 5,
        "assignment_completion_rate": 63,
        "attendance_percentage": 99,
        "social_media_hours": 3.1,
        "gaming_hours": 3.3,
        "stress_level": 9,
        "motivation_level": 6,
        "focus_score": 7,
        "procrastination_index": 10,
        "mental_state": 'Burnout',
        "sleep_hours": 6,
        "financial_stress": 7,
        "revision_efficiency":46,
        "burnout_risk": 4,
        "consistency_score": 1
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

