from pathlib import Path

import joblib
import pandas as pd


project_root = Path(__file__).resolve().parents[2]
ml_dir = project_root / "ml"
model_path = ml_dir / "student_rf.pkl"
feature_columns_path = ml_dir / "feature_columns.pkl"

loaded_object = joblib.load(model_path)
feature_columns = joblib.load(feature_columns_path)


def predict_final_exam_score(student_data):
	prediction_input = pd.DataFrame([student_data])
	prediction_input = pd.get_dummies(prediction_input, drop_first=True)
	prediction_input = prediction_input.reindex(columns=feature_columns, fill_value=0)

	prediction = loaded_object.predict(prediction_input)
	return float(prediction[0])

